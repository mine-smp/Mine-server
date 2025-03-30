#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import concurrent.futures
import requests
from bs4 import BeautifulSoup
import time
import json
import os
import sys
import re
import hashlib
import random
from datetime import datetime

# تنظیمات پیشرفته رنگ و استایل
class HackStyle:
    class Colors:
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        BRIGHT_BLACK = '\033[90m'
        BRIGHT_RED = '\033[91m'
        BRIGHT_GREEN = '\033[92m'
        BRIGHT_YELLOW = '\033[93m'
        BRIGHT_BLUE = '\033[94m'
        BRIGHT_MAGENTA = '\033[95m'
        BRIGHT_CYAN = '\033[96m'
        BRIGHT_WHITE = '\033[97m'
        END = '\033[0m'
    
    class Styles:
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        BLINK = '\033[5m'
        REVERSE = '\033[7m'
    
    @staticmethod
    def random_color():
        colors = [
            HackStyle.Colors.RED, HackStyle.Colors.GREEN, HackStyle.Colors.YELLOW,
            HackStyle.Colors.BLUE, HackStyle.Colors.MAGENTA, HackStyle.Colors.CYAN,
            HackStyle.Colors.BRIGHT_RED, HackStyle.Colors.BRIGHT_GREEN,
            HackStyle.Colors.BRIGHT_YELLOW, HackStyle.Colors.BRIGHT_BLUE,
            HackStyle.Colors.BRIGHT_MAGENTA, HackStyle.Colors.BRIGHT_CYAN
        ]
        return random.choice(colors)
    
    @staticmethod
    def hacker_text(text):
        chars = list(text)
        for i in range(len(chars)):
            if random.random() < 0.3:
                chars[i] = f"{HackStyle.random_color()}{chars[i]}{HackStyle.Colors.END}"
        return ''.join(chars)

# ابزارهای نمایش پیشرفته
class HackerUI:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_banner():
        HackerUI.clear_screen()
        banner = f"""
{HackStyle.Colors.BRIGHT_RED}
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{HackStyle.Colors.BRIGHT_CYAN}
    ╔═══════════════════════════════════════════════╗
    ║  {HackStyle.hacker_text("Advanced Port Scanner v3.0")}             ║
    ║  {HackStyle.hacker_text("Cyber Security Tool")}                    ║
    ║  {HackStyle.hacker_text("Developed by MINE ")}        ║
    ╚═══════════════════════════════════════════════╝
{HackStyle.Colors.END}
        """
        print(banner)
    
    @staticmethod
    def print_loading(progress=0, width=40):
        colors = [HackStyle.Colors.BRIGHT_RED, HackStyle.Colors.BRIGHT_YELLOW, HackStyle.Colors.BRIGHT_GREEN]
        filled = int(round(width * progress / 100))
        bar = colors[2] + '█' * filled + colors[0] + '░' * (width - filled) + HackStyle.Colors.END
        sys.stdout.write(f"\r[{bar}] {progress}%")
        sys.stdout.flush()
    
    @staticmethod
    def print_matrix_effect(lines=1):
        chars = "01"
        for _ in range(lines):
            print(' '.join(random.choice(chars) for _ in range(80)), end='\r')
    
    @staticmethod
    def print_status(message, status_type="info"):
        colors = {
            "info": HackStyle.Colors.BRIGHT_CYAN,
            "success": HackStyle.Colors.BRIGHT_GREEN,
            "warning": HackStyle.Colors.BRIGHT_YELLOW,
            "error": HackStyle.Colors.BRIGHT_RED,
            "critical": HackStyle.Colors.BRIGHT_MAGENTA
        }
        prefix = {
            "info": "[*]",
            "success": "[+]",
            "warning": "[!]",
            "error": "[-]",
            "critical": "[X]"
        }
        color = colors.get(status_type, HackStyle.Colors.BRIGHT_WHITE)
        print(f"{color}{prefix[status_type]} {message}{HackStyle.Colors.END}")

# توابع اصلی اسکنر
class PortScanner:
    @staticmethod
    def scan_port(target, port, timeout=1.0):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((target, port))
                if result == 0:
                    service = PortScanner.get_service_name(port)
                    return port, service
        except Exception:
            return None
    
    @staticmethod
    def get_service_name(port):
        services = {
            20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
            25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3",
            143: "IMAP", 443: "HTTPS", 445: "SMB", 3389: "RDP",
            5900: "VNC", 27017: "MongoDB", 3306: "MySQL",
            8080: "HTTP-ALT", 8443: "HTTPS-ALT", 22: "SSH",
            161: "SNMP", 162: "SNMP-TRAP", 389: "LDAP",
            636: "LDAPS", 1433: "MSSQL", 1521: "Oracle",
            5432: "PostgreSQL", 6379: "Redis", 9200: "Elasticsearch"
        }
        return services.get(port, "UNKNOWN")

class VulnerabilityScanner:
    @staticmethod
    def check_web_vulnerabilities(target, port, proxy=None):
        vulnerabilities = []
        try:
            protocol = "https" if port in [443, 8443] else "http"
            url = f"{protocol}://{target}:{port}"
            
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            }
            
            response = requests.get(url, headers=headers, proxies=proxies, timeout=5, verify=False)
            
            # بررسی هدرها
            server = response.headers.get("Server", "").lower()
            powered_by = response.headers.get("X-Powered-By", "").lower()
            
            if any(v in server for v in ["apache/2.2.", "apache/2.0", "apache/1."]):
                vulnerabilities.append("وب سرور قدیمی Apache (آسیب‌پذیر)")
            
            if "php" in powered_by and any(v in powered_by for v in ["php/5.", "php/4."]):
                vulnerabilities.append("نسخه قدیمی PHP (آسیب‌پذیر)")
            
            # بررسی مسیرهای حساس
            sensitive_paths = ["/phpinfo.php", "/test.php", "/admin/", "/wp-admin/", "/.git/"]
            if any(path in response.text.lower() for path in sensitive_paths):
                vulnerabilities.append("مسیرهای حساس شناسایی شد")
            
            # بررسی سیستم‌های مدیریت محتوا
            if "wp-content" in response.text.lower():
                vulnerabilities.append("وردپرس شناسایی شد (بررسی آسیب‌پذیری‌های وردپرس)")
            
            if "joomla" in response.text.lower():
                vulnerabilities.append("جوملا شناسایی شد (بررسی آسیب‌پذیری‌های جوملا)")
            
        except Exception as e:
            HackerUI.print_status(f"خطا در بررسی آسیب‌پذیری‌های وب: {str(e)}", "error")
        
        return vulnerabilities
    
    @staticmethod
    def check_service_vulnerabilities(port, service, target):
        vulnerabilities = []
        
        if port == 21 and "FTP" in service.upper():
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(2)
                    s.connect((target, port))
                    banner = s.recv(1024).decode(errors="ignore").lower()
                    
                    if "vsftpd 2.3.4" in banner:
                        vulnerabilities.append("FTP - آسیب‌پذیری backdoor vsftpd 2.3.4")
                    elif "anonymous" in banner:
                        vulnerabilities.append("FTP - دسترسی ناشناس فعال است")
            except:
                pass
        
        elif port == 22 and "SSH" in service.upper():
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(2)
                    s.connect((target, port))
                    banner = s.recv(1024).decode(errors="ignore").lower()
                    
                    if "openssh_7." in banner:
                        vulnerabilities.append("SSH - نسخه قدیمی OpenSSH (آسیب‌پذیر)")
                    if "libssh" in banner:
                        vulnerabilities.append("SSH - کتابخانه آسیب‌پذیر libssh")
            except:
                pass
        
        elif port == 445 and "SMB" in service.upper():
            vulnerabilities.append("SMB - بررسی آسیب‌پذیری‌های EternalBlue و SMBv1")
        
        elif port == 3389 and "RDP" in service.upper():
            vulnerabilities.append("RDP - ممکن است در معرض حملات Brute Force باشد")
        
        return vulnerabilities

class MalwareDetector:
    @staticmethod
    def scan_for_malware(target, port, proxy=None):
        indicators = []
        try:
            protocol = "https" if port in [443, 8443] else "http"
            url = f"{protocol}://{target}:{port}"
            
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            }
            
            response = requests.get(url, headers=headers, proxies=proxies, timeout=5, verify=False)
            content = response.text.lower()
            
            # الگوهای بدافزار
            patterns = {
                "eval(": r'eval\(.*\)',
                "base64_decode": r'base64_decode\(',
                "shell_exec": r'shell_exec\(.*\)',
                "crypto_miner": r'coinimp|miner|coinhive|cryptonight',
                "malicious_redirect": r'window\.location\s*=\s*["\']http',
                "suspicious_iframe": r'<iframe[^>]+src=["\']http[s]?://[^"\']+["\']'
            }
            
            for name, pattern in patterns.items():
                if re.search(pattern, content):
                    indicators.append(f"الگوی {name} شناسایی شد")
            
            # بررسی هش محتوا
            content_hash = hashlib.sha256(response.content).hexdigest()
            known_malware_hashes = [
                "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3",  # مثال
                "5d41402abc4b2a76b9719d911017c592"           # مثال
            ]
            if content_hash in known_malware_hashes:
                indicators.append(f"مطابقت با بدافزار شناخته شده (هش: {content_hash[:8]}...)")
            
        except Exception as e:
            HackerUI.print_status(f"خطا در بررسی بدافزار: {str(e)}", "error")
        
        return indicators

# مدیریت گزارش‌ها
class ReportManager:
    @staticmethod
    def generate_report(target, scan_data, vuln_data, malware_data):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report = {
            "meta": {
                "target": target,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "scan_duration": scan_data["duration"]
            },
            "open_ports": scan_data["open_ports"],
            "vulnerabilities": vuln_data,
            "malware_indicators": malware_data
        }
        return report
    
    @staticmethod
    def save_report(report, format="json"):
        filename = f"scan_report_{report['meta']['target']}_{report['meta']['date'].replace(' ', '_').replace(':', '')}"
        
        if format == "json":
            filename += ".json"
            with open(filename, "w") as f:
                json.dump(report, f, indent=4)
        else:
            filename += ".txt"
            with open(filename, "w") as f:
                f.write(f"گزارش اسکن امنیتی\n")
                f.write(f"هدف: {report['meta']['target']}\n")
                f.write(f"تاریخ: {report['meta']['date']}\n")
                f.write(f"مدت زمان اسکن: {report['meta']['scan_duration']} ثانیه\n\n")
                
                f.write("پورت‌های باز:\n")
                for port, service in report["open_ports"]:
                    f.write(f"  {port}/tcp - {service}\n")
                
                f.write("\nآسیب‌پذیری‌ها:\n")
                for vuln in report["vulnerabilities"]:
                    f.write(f"  - {vuln}\n")
                
                f.write("\nنشانه‌های بدافزار:\n")
                for mal in report["malware_indicators"]:
                    f.write(f"  - {mal}\n")
        
        HackerUI.print_status(f"گزارش در فایل {filename} ذخیره شد", "success")

# رابط کاربری اصلی
class HackerInterface:
    @staticmethod
    def get_target():
        HackerUI.print_banner()
        HackerUI.print_status("لطفاً آدرس هدف را وارد کنید (IP یا دامنه):", "info")
        print(f"{HackStyle.Colors.BRIGHT_GREEN}[>>>] {HackStyle.Colors.END}", end="")
        target = input().strip()
        return target
    
    @staticmethod
    def get_port_range():
        HackerUI.print_status("انتخاب محدوده پورت‌ها:", "info")
        print(f"{HackStyle.Colors.BRIGHT_YELLOW}[1] همه پورت‌ها (1-65535)")
        print("[2] پورت‌های رایج (1-1024)")
        print("[3] پورت‌های وب (80,443,8080,8443)")
        print("[4] محدوده دلخواه (مثال: 20-80 یا 22)")
        print(f"{HackStyle.Colors.END}", end="")
        
        while True:
            try:
                choice = int(input(f"{HackStyle.Colors.BRIGHT_GREEN}[>>>] {HackStyle.Colors.END}"))
                if choice == 1:
                    return (1, 65535)
                elif choice == 2:
                    return (1, 1024)
                elif choice == 3:
                    return (80, 8443)  # شامل همه پورت‌های وب
                elif choice == 4:
                    custom = input("محدوده را وارد کنید (مثال: 20-80 یا 22): ").strip()
                    if '-' in custom:
                        start, end = map(int, custom.split('-'))
                        return (start, end)
                    else:
                        port = int(custom)
                        return (port, port)
                else:
                    HackerUI.print_status("گزینه نامعتبر! لطفاً عدد بین 1 تا 4 وارد کنید", "error")
            except ValueError:
                HackerUI.print_status("ورودی نامعتبر! لطفاً عدد وارد کنید", "error")
    
    @staticmethod
    def get_proxy():
        HackerUI.print_status("آیا می‌خواهید از پروکسی استفاده کنید؟ (y/n):", "info")
        proxy_choice = input(f"{HackStyle.Colors.BRIGHT_GREEN}[>>>] {HackStyle.Colors.END}").lower()
        if proxy_choice == 'y':
            HackerUI.print_status("آدرس پروکسی را وارد کنید (مثال: 127.0.0.1:8080):", "info")
            proxy = input(f"{HackStyle.Colors.BRIGHT_GREEN}[>>>] {HackStyle.Colors.END}").strip()
            return proxy
        return None
    
    @staticmethod
    def show_results(target, open_ports, vulnerabilities, malware_indicators, scan_time):
        HackerUI.clear_screen()
        HackerUI.print_banner()
        
        print(f"\n{HackStyle.Colors.BRIGHT_CYAN}═════════ نتایج اسکن ═════════{HackStyle.Colors.END}")
        print(f"{HackStyle.Colors.BRIGHT_WHITE}هدف:{HackStyle.Colors.END} {target}")
        print(f"{HackStyle.Colors.BRIGHT_WHITE}مدت زمان اسکن:{HackStyle.Colors.END} {scan_time:.2f} ثانیه")
        
        print(f"\n{HackStyle.Colors.BRIGHT_GREEN}═════════ پورت‌های باز ═════════{HackStyle.Colors.END}")
        for port, service in open_ports:
            print(f"  {HackStyle.Colors.BRIGHT_YELLOW}{port}/tcp{HackStyle.Colors.END} - {service}")
        
        if vulnerabilities:
            print(f"\n{HackStyle.Colors.BRIGHT_RED}═════════ آسیب‌پذیری‌ها ═════════{HackStyle.Colors.END}")
            for vuln in vulnerabilities:
                print(f"  {HackStyle.Colors.BRIGHT_RED}- {vuln}{HackStyle.Colors.END}")
        
        if malware_indicators:
            print(f"\n{HackStyle.Colors.BRIGHT_MAGENTA}═════════ نشانه‌های بدافزار ═════════{HackStyle.Colors.END}")
            for mal in malware_indicators:
                print(f"  {HackStyle.Colors.BRIGHT_MAGENTA}- {mal}{HackStyle.Colors.END}")
        
        print(f"\n{HackStyle.Colors.BRIGHT_CYAN}══════════════════════════════{HackStyle.Colors.END}")

# اجرای اصلی برنامه
def main():
    try:
        # دریافت اطلاعات از کاربر
        target = HackerInterface.get_target()
        port_range = HackerInterface.get_port_range()
        proxy = HackerInterface.get_proxy()
        
        # شروع اسکن
        HackerUI.clear_screen()
        HackerUI.print_banner()
        HackerUI.print_status(f"شروع اسکن {target} از پورت {port_range[0]} تا {port_range[1]}...", "info")
        
        open_ports = []
        start_time = time.time()
        
        # اسکن پورت‌ها با نمایش پیشرفت
        total_ports = port_range[1] - port_range[0] + 1
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(PortScanner.scan_port, target, port): port 
                      for port in range(port_range[0], port_range[1] + 1)}
            
            for i, future in enumerate(concurrent.futures.as_completed(futures)):
                progress = (i + 1) / total_ports * 100
                HackerUI.print_loading(progress)
                
                result = future.result()
                if result:
                    open_ports.append(result)
        
        scan_time = time.time() - start_time
        
        # بررسی آسیب‌پذیری‌ها و بدافزارها
        vulnerabilities = []
        malware_indicators = []
        
        for port, service in open_ports:
            # بررسی آسیب‌پذیری‌ها
            if service.upper() in ["HTTP", "HTTPS", "HTTP-ALT", "HTTPS-ALT"]:
                vulns = VulnerabilityScanner.check_web_vulnerabilities(target, port, proxy)
                vulnerabilities.extend(vulns)
            
            service_vulns = VulnerabilityScanner.check_service_vulnerabilities(port, service, target)
            vulnerabilities.extend(service_vulns)
            
            # بررسی بدافزارها
            if service.upper() in ["HTTP", "HTTPS", "HTTP-ALT", "HTTPS-ALT"]:
                malware = MalwareDetector.scan_for_malware(target, port, proxy)
                malware_indicators.extend(malware)
        
        # نمایش نتایج
        HackerInterface.show_results(target, open_ports, vulnerabilities, malware_indicators, scan_time)
        
        # ذخیره گزارش
        report = ReportManager.generate_report(
            target,
            {"open_ports": open_ports, "duration": scan_time},
            vulnerabilities,
            malware_indicators
        )
        
        HackerUI.print_status("آیا می‌خواهید گزارش را ذخیره کنید؟ (y/n):", "info")
        save_choice = input(f"{HackStyle.Colors.BRIGHT_GREEN}[>>>] {HackStyle.Colors.END}").lower()
        if save_choice == 'y':
            ReportManager.save_report(report)
        
        HackerUI.print_status("اسکن کامل شد! برای خروج Enter بزنید...", "success")
        input()
    
    except KeyboardInterrupt:
        HackerUI.print_status("اسکن توسط کاربر متوقف شد!", "error")
        exit(1)
    except Exception as e:
        HackerUI.print_status(f"خطای غیرمنتظره: {str(e)}", "critical")
        exit(1)

if __name__ == "__main__":
    main()
