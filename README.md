# 🚀 SpeedTest 流量消耗器

[![Python版本](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![授權協議](https://img.shields.io/badge/License-MIT-green)](LICENSE)

自動化網絡流量消耗工具，基於 Speedtest.net 的測速協議實現

## 🌟 功能亮點
- 🔁 自動循環執行網絡測速
- 📶 實時顯示上下行帶寬
- 🧮 智能流量消耗估算
- 🌐 支持全球伺服器選擇
- ⚡ 雙版本支持 (Python/Bash)

## ⚠️ 法律與服務條款警告

- 使用前請確認您的網絡服務提供商政策

- 禁止用於任何非法用途

## 🛠️ 安裝指南

### 前置需求
- Python 3.6+ 或 Bash 環境
- 100MB 以上可用磁盤空間
- 穩定的網絡連接

### 依賴安裝
```bash
# Python 版本 (推薦)
git clone https://github.com/LilWang3399/speedtest-traffic-consumer.git
cd speedtest-traffic-consumer
python src/main.py --interval 300

# Bash 版本 (Debian/Ubuntu)
wget https://raw.githubusercontent.com/LilWang3399/speedtest-traffic-consumer/main/scripts/speedtest.sh
chmod +x speedtest.sh
./speedtest.sh --no-upload
