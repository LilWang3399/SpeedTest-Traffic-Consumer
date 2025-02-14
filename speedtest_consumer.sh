#!/bin/bash

echo "流量消耗腳本啟動 (按 Ctrl+C 停止)"

while true; do
    echo "開始新一輪測速..."
    speedtest --simple
    echo "準備下一次測速..."
    sleep 10  # 可調整間隔時間（秒）
done
