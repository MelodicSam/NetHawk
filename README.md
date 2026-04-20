<div align="center">

```
  _   _      _   _   _               _    
 | \ | | ___| |_| | | | __ ___      | | __
 |  \| |/ _ \ __| |_| |/ _` \ \ /\ / /| |/ /
 | |\  |  __/ |_|  _  | (_| |\ V  V / |   < 
 |_| \_|\___|\__|_| |_|\__,_| \_/\_/  |_|\_\
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=3000&pause=1000&color=00D9FF&center=true&vCenter=true&width=500&lines=Network+Reconnaissance+Toolkit;Scan.+Analyze.+Enumerate." alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Kali-557C94?style=for-the-badge&logo=linux&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-22c55e?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-00D9FF?style=for-the-badge)
![Terminal](https://img.shields.io/badge/Interface-Terminal-black?style=for-the-badge&logo=windowsterminal&logoColor=white)

<br/>

> **NetHawk is a Python-based network reconnaissance toolkit for security students and professionals. It provides a clean, menu-driven terminal interface for network scanning, port enumeration, IP intelligence, and more.**

⚠️ **For educational and authorized use only.**

</div>

---

## 🎯 Features

| # | Tool | Description |
|---|------|-------------|
| 1 | 📡 **Network Scanner** | Discover all live hosts on a subnet using ICMP ping sweep |
| 2 | 🔍 **Port Scanner** | Scan common or full port range, detect services & banners |
| 3 | 🌐 **IP Info Lookup** | Geolocation, ISP, ASN, timezone for any IP address |
| 4 | 💻 **My Network Info** | Show local IP, public IP, gateway, interfaces, DNS |
| 5 | 🔀 **MAC Changer** | Randomize or set a custom MAC address on any interface |

---

## 📸 Preview

```
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

```bash
# Clone the repository
git clone https://github.com/MelodicSam/nethawk.git
cd nethawk

# Run setup (installs all dependencies)
sudo bash setup.sh
```

### Manual install (without setup.sh)

```bash
pip install -r requirements.txt --break-system-packages
chmod +x nethawk.py
```

---

## ▶️ Usage

```bash
# Run directly
python3 nethawk.py

# Or if setup.sh was run
nethawk
```

> Most features work without root. MAC Changer requires `sudo`.

---

## 📂 Project Structure

```
📁 nethawk/
├── 📄 nethawk.py        # Main toolkit script
├── 📄 setup.sh          # Auto-installer
├── 📄 requirements.txt  # Python dependencies
└── 📄 README.md         # Documentation
```

---

## 🛠️ Built With

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/Rich_Library-Terminal_UI-grey?style=for-the-badge&logo=pypi&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-00D9FF?style=for-the-badge)
![Linux](https://img.shields.io/badge/iproute2-Linux_Networking-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## 📚 What I Learned

- Building **menu-driven CLI tools** in Python
- **Socket programming** for port scanning
- Using **subprocess** to run Linux network commands
- Parsing **IP routing tables** programmatically
- Fetching and displaying **geolocation data** from REST APIs
- **MAC address** structure and how to change it at the OS level

---

## 🔮 Upcoming Features

- [ ] ARP spoofing detection
- [ ] Banner grabbing improvements
- [ ] Export scan results to JSON / CSV
- [ ] Traceroute visualization
- [ ] Vulnerability CVE lookup by service version

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **authorized penetration testing only**. The author is not responsible for any misuse or damage caused by this program. Always get proper authorization before scanning any network.

---

## 👤 Author

<div align="center">

**Swayam Patel**

[![GitHub](https://img.shields.io/badge/GitHub-MelodicSam-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MelodicSam)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Swayam_Patel-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/swayam-patel-131b84339/)
[![Email](https://img.shields.io/badge/Email-swayampatel2827@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:swayampatel2827@gmail.com)

</div>

---

## 📄 License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

---

<div align="center">

**If this helped you learn something, drop a ⭐ — it means a lot!**

![Wave](https://raw.githubusercontent.com/mayhemantt/mayhemantt/Update/svg/Bottom.svg)

</div>
