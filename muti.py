import time
import os
import sys
import threading

def check_dependency():
    try:
        from speedtest import Speedtest
        return True
    except ImportError:
        print("未檢測到 speedtest-cli 庫，正在嘗試安裝...")
        try:
            os.system(f"{sys.executable} -m pip install speedtest-cli")
            return True
        except Exception as e:
            print(f"安裝失敗: {str(e)}")
            return False

def run_speedtest(thread_id):
    from speedtest import Speedtest
    st = Speedtest()
    
    print(f"線程 {thread_id}: 正在獲取伺服器列表...")
    st.get_servers()
    
    print(f"線程 {thread_id}: 選擇最佳伺服器...")
    best = st.get_best_server()
    print(f"線程 {thread_id}: 已選擇: {best['host']} ({best['country']})")
    
    print(f"線程 {thread_id}: 開始下載測速...")
    download_speed = st.download() / 1_000_000  # 轉換為 Mbps
    print(f"線程 {thread_id}: 下載速度: {download_speed:.2f} Mbps")
    
    print(f"線程 {thread_id}: 開始上傳測速...")
    upload_speed = st.upload() / 1_000_000  # 轉換為 Mbps
    print(f"線程 {thread_id}: 上傳速度: {upload_speed:.2f} Mbps")
    
    # 計算消耗流量
    elapsed = time.time() - start_time
    dl_data = download_speed * elapsed / 8  # MB
    ul_data = upload_speed * elapsed / 8   # MB
    total = dl_data + ul_data
    
    print(f"線程 {thread_id}: 本次循環消耗約 {total:.2f} MB 流量")
    print(f"線程 {thread_id}: 準備下一次測速...\n")

def speedtest_thread(thread_id, stop_event):
    while not stop_event.is_set():
        run_speedtest(thread_id)
        time.sleep(1)  # 每次測試間隔 1 秒

if __name__ == "__main__":
    if not check_dependency():
        print("請手動安裝 speedtest-cli: pip install speedtest-cli")
        sys.exit(1)
    
    print("流量消耗腳本已啟動 (按 Ctrl+C 停止)")
    
    # 設置停止事件
    stop_event = threading.Event()
    
    # 創建多個線程
    num_threads = 4  # 可以根據需要調整線程數量
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=speedtest_thread, args=(i, stop_event))
        thread.start()
        threads.append(thread)
    
    try:
        while True:
            time.sleep(1)  # 主線程保持運行
    except KeyboardInterrupt:
        print("\n正在停止所有線程...")
        stop_event.set()  # 通知所有線程停止
        for thread in threads:
            thread.join()  # 等待所有線程結束
        print("腳本已停止")
