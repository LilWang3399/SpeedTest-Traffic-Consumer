import time
import os
import sys

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

def run_speedtest():
    from speedtest import Speedtest
    st = Speedtest()
    
    print("正在獲取伺服器列表...")
    st.get_servers()
    
    print("選擇最佳伺服器...")
    best = st.get_best_server()
    print(f"已選擇: {best['host']} ({best['country']})")
    
    print("開始下載測速...")
    download_speed = st.download() / 1_000_000  # 轉換為 Mbps
    print(f"下載速度: {download_speed:.2f} Mbps")
    
    print("開始上傳測速...")
    upload_speed = st.upload() / 1_000_000  # 轉換為 Mbps
    print(f"上傳速度: {upload_speed:.2f} Mbps")
    
    return download_speed, upload_speed

if __name__ == "__main__":
    if not check_dependency():
        print("請手動安裝 speedtest-cli: pip install speedtest-cli")
        sys.exit(1)
    
    print("流量消耗腳本已啟動 (按 Ctrl+C 停止)")
    
    try:
        while True:
            start_time = time.time()
            download, upload = run_speedtest()
            elapsed = time.time() - start_time
            
            # 估算消耗流量（理論最大值）
            dl_data = download * elapsed / 8  # MB
            ul_data = upload * elapsed / 8   # MB
            total = dl_data + ul_data
            
            print(f"本次循環消耗約 {total:.2f} MB 流量")
            print("準備下一次測速...\n")
            
    except KeyboardInterrupt:
        print("\n腳本已停止")
