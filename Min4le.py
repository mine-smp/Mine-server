from pyfiglet import Figlet
from termcolor import colored
import os
from time import sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    clear_screen()
    header = """
    ███╗   ███╗██╗███╗   ██╗███████╗  █████╗ ██████╗ ████████╗
    ████╗ ████║██║████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝
    ██╔████╔██║██║██╔██╗ ██║█████╗   ███████║██████╔╝   ██║   
    ██║╚██╔╝██║██║██║╚██╗██║██╔══╝   ██╔══██║██╔═══╝    ██║   
    ██║ ╚═╝ ██║██║██║ ╚████║███████╗ ██║  ██║██║        ██║   
    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═╝  ╚═╝╚═╝        ╚═╝   
    """
    print(colored(header, 'cyan'))
    print(colored("="*60, 'blue'))
    print(colored(" ابزار حرفه ای ساخت متن های ASCII با رنگ دلخواه ", 'yellow'))
    print(colored("="*60, 'blue'))
    print()

def get_user_choice(options, prompt):
    while True:
        try:
            print(prompt)
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            
            choice = int(input("\nلطفاً عدد مربوط به گزینه مورد نظر را انتخاب کنید: "))
            if 1 <= choice <= len(options):
                return choice - 1
            else:
                print(colored("\n⚠️ خطا: عدد وارد شده خارج از محدوده است. لطفاً دوباره تلاش کنید.", 'red'))
                sleep(1)
        except ValueError:
            print(colored("\n⚠️ خطا: لطفاً فقط عدد وارد کنید.", 'red'))
            sleep(1)

def create_ascii_art():
    display_header()
    
    # دریافت متن از کاربر
    text = input("\n✏️ متن مورد نظر خود را وارد کنید: ")
    
    # لیست فونت‌های موجود
    fonts = [
        'standard', 'big', 'block', 'bubble', 'digital',
        'lean', 'mini', 'script', 'shadow', 'slant',
        '3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator'
    ]
    
    # لیست رنگ‌های متن
    text_colors = [
        'grey', 'red', 'green', 'yellow', 'blue',
        'magenta', 'cyan', 'white'
    ]
    
    # لیست رنگ‌های پس‌زمینه
    highlight_colors = [
        'on_grey', 'on_red', 'on_green', 'on_yellow',
        'on_blue', 'on_magenta', 'on_cyan', 'on_white'
    ]
    
    # انتخاب فونت
    font_choice = get_user_choice(fonts, "\n🎨 لطفاً فونت مورد نظر را انتخاب کنید:")
    selected_font = fonts[font_choice]
    
    # انتخاب رنگ متن
    text_color_choice = get_user_choice(text_colors, "\n🌈 لطفاً رنگ متن را انتخاب کنید:")
    selected_text_color = text_colors[text_color_choice]
    
    # انتخاب رنگ پس‌زمینه
    highlight_choice = get_user_choice(highlight_colors, "\n🎨 لطفاً رنگ پس‌زمینه را انتخاب کنید:")
    selected_highlight = highlight_colors[highlight_choice]
    
    # ساخت ASCII Art
    figlet = Figlet(font=selected_font)
    ascii_art = figlet.renderText(text)
    
    # نمایش نتیجه نهایی
    display_header()
    print("\n✨ نتیجه نهایی:\n")
    print(colored(ascii_art, selected_text_color, selected_highlight))
    
    # گزینه ذخیره در فایل
    save_choice = input("\nآیا می‌خواهید خروجی را در فایل ذخیره کنید؟ (y/n): ").lower()
    if save_choice == 'y':
        filename = input("نام فایل را وارد کنید (بدون پسوند): ") + ".txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(ascii_art)
        print(colored(f"\n✅ فایل با نام '{filename}' ذخیره شد.", 'green'))
    
    # تکرار برنامه
    repeat = input("\nآیا می‌خواهید متن دیگری ایجاد کنید؟ (y/n): ").lower()
    if repeat == 'y':
        create_ascii_art()
    else:
        print(colored("\n🙏 با تشکر از استفاده شما از این برنامه. خدانگهدار!", 'magenta'))

if __name__ == "__main__":
    try:
        create_ascii_art()
    except ImportError:
        print(colored("برای اجرای این کد نیاز به نصب کتابخانه‌های زیر دارید:", 'red'))
        print(colored("pip install pyfiglet termcolor", 'yellow'))
    except Exception as e:
        print(colored(f"خطایی رخ داد: {e}", 'red'))
