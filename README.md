<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=180&section=header&text=NetHawk&fontSize=52&fontAlignY=35&desc=Network%20Reconnaissance%20Toolkit&descAlignY=55&color=0:0f172a,50:0ea5e9,100:22d3ee"/>

# 🦅 NetHawk

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2800&pause=900&color=00D9FF&center=true&vCenter=true&width=700&lines=Network+Reconnaissance+Toolkit;Scan+%E2%80%A2+Analyze+%E2%80%A2+Enumerate;Built+with+Python+for+security+students+and+professionals" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Kali-557C94?style=for-the-badge&logo=linux&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-Terminal-111827?style=for-the-badge&logo=gnometerminal&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-06b6d4?style=for-the-badge)
![License](https://img.shields.io/badge/License-GPL--3.0-22c55e?style=for-the-badge)

<br/><br/>

> **NetHawk** is a Python-based **network reconnaissance toolkit** built for **security students, homelab users, and professionals**.  
> It provides a clean, menu-driven CLI for **host discovery, port scanning, IP intelligence, and local network inspection**.

⚠️ **For educational and authorized use only.**

</div>

---

## ✨ Why NetHawk?

NetHawk is designed to make common reconnaissance tasks easier from one clean terminal interface. Instead of jumping between multiple commands, you get a focused toolkit that helps you quickly inspect networks, enumerate services, and gather useful IP information in one place.

---

## 🎯 Features

| # | Module | What it does |
|---|--------|---------------|
| 1 | 📡 **Network Scanner** | Discover live hosts on a subnet with an ICMP ping sweep |
| 2 | 🔍 **Port Scanner** | Scan common ports or a wider range and inspect services / banners |
| 3 | 🌐 **IP Info Lookup** | Retrieve IP geolocation, ISP, ASN, and timezone details |
| 4 | 💻 **My Network Info** | View local IP, public IP, gateway, interfaces, and DNS details |
| 5 | 🔀 **MAC Changer** | Randomize or set a custom MAC address for an interface |

---

## 🖼️ Preview

```text
  _   _      _   _   _               _    
 | \ | | ___| |_| | | | __ ___      | | __
 |  \| |/ _ \ __| |_| |/ _` \ \ /\ / /| |/ /
 | |\  |  __/ |_|  _  | (_| |\ V  V / |   < 
 |_| \_|\___|\__|_| |_|\__,_| \_/\_/  |_|\_\

         Network Reconnaissance Toolkit
               by MelodicSam

 ┌─────────────────────────────────────┐
 │         NETHAWK MAIN MENU           │
 ├─────────────────────────────────────┤
 │  [1]  Network Scanner               │
 │  [2]  Port Scanner                  │
 │  [3]  IP Info Lookup                │
 │  [4]  My Network Info               │
 │  [5]  MAC Address Changer           │
 │  [0]  Exit                          │
 └─────────────────────────────────────┘

  nethawk →
```

---

## 🚀 Installation

### 1) Clone the repository

```bash
git clone https://github.com/MelodicSam/NetHawk.git
cd NetHawk
```

### 2) Run the setup script

```bash
sudo bash setup.sh
```

### Manual installation

```bash
pip install -r requirements.txt --break-system-packages
chmod +x nethawk.py
```

---

## ▶️ Usage

```bash
# Run directly
python3 nethawk.py

# Or if setup.sh added the launcher
nethawk
```

> Most features work without root privileges.  
> **MAC Changer requires `sudo`.**

---

## 📂 Project Structure

```text
NetHawk/
├── nethawk.py        # Main toolkit script
├── setup.sh          # Auto-installer
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## 🛠️ Built With

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-Terminal_UI-374151?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-HTTP-06b6d4?style=for-the-badge)
![Linux Networking](https://img.shields.io/badge/iproute2-Linux_Networking-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## 📚 What I Learned

- Building **menu-driven CLI tools** in Python
- Using **socket programming** for port scanning
- Running Linux networking commands with **subprocess**
- Parsing **routing and interface information**
- Fetching and displaying **IP intelligence data** from APIs
- Understanding **MAC address manipulation** at the OS level

---

## 🗺️ Roadmap

- [ ] Export scan results to JSON / CSV
- [ ] Improved banner grabbing
- [ ] Traceroute visualization
- [ ] CVE lookup by detected service version
- [ ] ARP spoofing detection

---

## ⚠️ Disclaimer

This project is intended for **educational use** and **authorized security testing only**.  
Do not scan systems or networks without proper permission. The author is not responsible for misuse or damage caused by this tool.

---

## 👤 Author

<div align="center">

**Swayam Patel**

[![GitHub](https://img.shields.io/badge/GitHub-MelodicSam-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MelodicSam)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Swayam_Patel-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/swayam-patel-131b84339/)
[![Email](https://img.shields.io/badge/Email-swayampatel2827%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:swayampatel2827@gmail.com)

</div>

---

## 🌟 Support

If this project helped you learn something, consider giving it a **star** on GitHub.

---

<div align="center">

<img width="100%" src="https://raw.githubusercontent.com/MelodicSam/NetHawk/main/assets/bottom.svg"/>

</div>
