# المحاضرة 5 — الواجب | Introduction to OOP

**Engineer Ibrahim — كورس Python & AI (12 محاضرة) · أسئلة المحاضرة 5**

الملف ده موجود في **نسختين بنفس المحتوى**: `L05_assignment.md` تنسخ منه بلوك
بلوك بضغطة من GitHub أو Colab، و `L05_assignment.pdf` لو بتحب تطبع وتشتغل على
ورق. اختار اللي يريحك.

**التسليم على GitHub — في نيوتبوكين من إيدك أنت:**

- `lectures/lecture_05/exercises.ipynb` → حلول **الجزء A**
- `lectures/lecture_05/tracker_v3.ipynb` → **الجزء B + C**: المينيو بقى كائنات
  (قطعة المشروع)
- `tracker/models.py` → الكلاسات نفسها، في جذر الريبو (اترفع من متصفح GitHub)

**تحقق ذاتي:** كل سؤال ليه **checklist** تتأكّد منه بعينك و/أو **assert** —
كل واحد بيقول `ممتاز` أو يوضّح الغلط.

**سياسة AI:** تشرحلك وتلاقي الغلط — **ما تكتبشلك الحل**. الهدف إنك أنت تتعلم.

مدة الواجب 2–3 ساعات — يتسلّم قبل المحاضرة 6.

---

## الجزء A — تمارين المهارات (5 تمارين)

### A1 — كلاس طالب بمتوسط درجات

عرّف كلاس `Student`: `__init__` ياخذ الاسم والدرجات ويخزّنهم على الكائن،
و method اسمه `average` يرجّع متوسط الدرجات (حساب بـ `for` بس — من غير
`sum()`، ده تثبيت للوبات).

```python
class Student:
    def __init__(self, name, grades):
        # TODO: خزّن الاسم والدرجات من المعاملات — استبدل المؤقت
        self.name = "?"
        self.grades = []

    def average(self):
        # TODO: لفّ على الدرجات ورجّع المتوسط (ناتج مؤقت)
        return 0

s = Student("Sara", [85, 90, 76])
print(s.name)
```

**تحقق ذاتي:**

```python
assert s.name == "Sara", "الاسم اتخزّن على الكائن"
assert abs(s.average() - 83.67) < 0.01, "متوسط سارة"
t = Student("Omar", [70, 80])
assert t.name == "Omar", "كل طالب ليه اسمه"
assert abs(t.average() - 75.0) < 0.01, "متوسط عمر"
print("A1: ممتاز")
```

---

### A2 — حساب بنكي بحماية من السحب الزايد

كلاس `BankAccount`: `__init__` ياخذ اسم المالك ورصيد افتراضي صفر، و
`deposit` يزوّد الرصيد، و `withdraw` يخصم **بس لو فيه رصيد كافي** — غير كده
اطبع `رصيد غير كافٍ` وسيب الرصيد زي ما هو.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        # TODO: خزّن اسم المالك والرصيد
        pass

    def deposit(self, amount):
        # TODO: زوّد الرصيد بمبلغ الإيداع
        pass

    def withdraw(self, amount):
        # TODO: لو المبلغ أكبر من الرصيد اطبع رسالة واقف — غير كده اخصم
        pass

acc = BankAccount("Omar", 100)
acc.deposit(50)
```

**تحقق ذاتي:**

```python
acc = BankAccount("Omar", 100)
acc.deposit(50)
assert acc.balance == 150, "الإيداع زوّد الرصيد"
acc.withdraw(40)
assert acc.balance == 110, "السحب خصم"
acc.withdraw(500)
assert acc.balance == 110, "الحماية من السحب الزايد"
assert BankAccount("Sara").balance == 0, "الرصيد الافتراضي صفر"
print("A2: ممتاز")
```

**Checklist:** سحب أكبر من الرصيد طبع رسالة واضحة وماخصمش · الرصيد الافتراضي
شغال من غير ما نمرّره · كل حساب ليه رصيده المستقل.

---

### A3 — `__str__` لطيف

كلاس `Book`: لازم `__str__` يرجّع نص **بالشكل ده بالظبط**:
`"Python — 350 صفحة"`. من غيره `print(b)` هيطبع كلام تقني طويل زي
`<__main__.Book object at 0x...>`.

```python
class Book:
    def __init__(self, title, pages):
        # TODO: خزّن العنوان وعدد الصفحات
        pass

    def __str__(self):
        # TODO: رجّع النص بالشكل ده — شوف بلوك التحقق تحت
        return "؟؟؟"

b = Book("Python", 350)
print(b)
```

**تحقق ذاتي:**

```python
assert str(b) == "Python — 350 صفحة", "النص بالظبط زي المطلوب"
b2 = Book("Pandas", 500)
assert str(b2) == "Pandas — 500 صفحة", "كتاب تاني"
print("A3: ممتاز")
```

---

### A4 — قاعة صف فيها قائمة كائنات (أول composition)

كلاس `Classroom` بيمسك قائمة طلاب — نفس فكرة `Tracker` اللي جاي في الجزء B.
استخدم كلاس `Student` بتاع A1 اللي فوق (شغّل خلية A1 الأول).

```python
class Classroom:
    def __init__(self, room):
        # TODO: اسم القاعة + قائمة طلاب فاضية
        self.room = "?"
        self.students = []

    def add(self, student):
        # TODO: ضيف الطالب لقائمة الطلاب
        pass

    def best(self):
        # TODO: رجّع الطالب الأعلى بمتوسط الدرجات (لفّ على القائمة)
        return None

room = Classroom("A101")
room.add(Student("Sara", [85, 90, 76]))
```

**تحقق ذاتي:**

```python
assert room.room == "A101", "اسم القاعة"
assert len(room.students) == 1, "أول طالب اتضاف"
room.add(Student("Omar", [95, 95]))
assert len(room.students) == 2, "تاني طالب"
assert room.best().name == "Omar", "الأعلى بمتوسط يفوز"
print("A4: ممتاز")
```

---

### A5 — تتبّع على ورق: إيه اللي هيتطبع؟

اقرأ الكود ده **ورقًا الأول** واكتب الناتج المتوقع في `answer` — وبعدين
شغّل واتأكّد. السر في سطر واحد.

```python
class Counter:
    def __init__(self):
        self.n = 0

    def bump(self):
        self.n += 1
        return self.n

c1 = Counter()
c2 = Counter()
print(c1.bump(), c1.bump(), c2.bump())
```

```python
# اكتب الناتج كنص قبل ما تشغّل الخلية اللي فوق
answer = ""
# TODO: اكتب الناتج زي ما هو — المفروض تلات أرقام مفصولة بمسافات
assert answer == "1 2 1", "c1 و c2 مش نفس الكائن — اتفرّج تاني"
print("A5: ممتاز")
```

**Checklist:** توقعت الناتج قبل ما تشغّل · عرفت ليه `c2` بدأت من الأول ·
عرفت ليه `self` معناها "بتاعي" ومش رقم ثابت.

---

## الجزء B — قطعة المشروع: tracker/models.py + tracker_v3.ipynb

**ده أهم جزء.** من L4 عندك دوال في `tracker/functions.py` وبياناتك بتنقري
وبتتحفظ من CSV. النهاردة نرفعها **درجة**: نفس الشغل بس بـ **كائنات** —

- كل سجل بقى **كائن `Record`** بدل قاموس: بيانات + طرق على نفس الشيء.
- القائمة كلها جوّا **كائن `Tracker`** — وطرقه هي خيارات المينيو نفسها.
- المينيو `tracker_v3.ipynb` = نفس الثمانية خيارات بتوع L4 — بس كل خيار
  بقى **سطر قصير** بينادي method.

### الخطوات بالترتيب

1. خلية الإعداد (معطاة — شغّلها أول حاجة): تجهّز المجلدات.

```python
# tracker_v3.ipynb — شغّلها أول حاجة
import os
os.makedirs("tracker", exist_ok=True)
os.makedirs("data", exist_ok=True)
```

2. اكتب محتوى `tracker/models.py` في خلية جديدة — **أول سطر في الخلية**
   يكون `%%writefile tracker/models.py` وبعده المحتوى ده كله:

```python
# tracker/models.py
import csv


class Record:
    """One tracker row: the five project fields."""

    def __init__(self, date, category, amount_egp,
                 payment_method, quantity):
        # TODO: خزّن الحقول الخمسة على الكائن — المبلغ يتحفظ رقمًا
        pass

    def to_dict(self):
        # TODO: رجّع قاموس بالحقول الخمسة — بنفس الترتيب
        pass

    def __str__(self):
        # TODO: رجّع سطرًا منسّقًا يظهر مباشرة في الشاشة
        pass


class Tracker:
    """A list of Record objects + every behavior the menu needs."""

    def __init__(self):
        # TODO: self.records = قائمة فاضية
        pass

    def add(self, record):
        # TODO: ضيف الكائن لقائمة السجلات
        pass

    def filter_by(self, category):
        # TODO: قائمة جديدة بسجلات التصنيف المطلوب فقط
        pass

    def summary(self):
        # TODO: قاموس الملخص — العدد والمجموع والمتوسط والأعلى والأدنى
        #       للمبلغ الأساسي — ولو القائمة فاضية رجّع أصفار
        pass

    def save(self, path):
        # TODO: csv + to_dict — صف العناوين أول حاجة وبعده السجلات
        pass

    def load(self, path):
        # TODO: اقرأ الصفوف وحوّلها لسجلات الكائن داخل المتتبّع
        #       ملف مش موجود → سيب القائمة زي ما هي
        #       المبلغ لازم يرجع رقمًا بعد القراءة
        pass
```

**نصيحة:** تقدر تستورد دوالك من `tracker.functions` وتستغلّها جوّا الطرق —
مثلاً تحوّل السجلات بـ `to_dict()` وتستدعي `save_records` بدل ما تعيد
كتابة الـ CSV من الأول. اختيارك — والأهم إن الطريقة تشتغل.

3. استورد الكلاسات وحمّل بياناتك. لو الملف لسه فاضي، الصق سجلاتك من
   المحاضرة اللي فاتت ككائنات:

```python
from tracker.models import Record, Tracker

t = Tracker()
t.load("data/sample_records.csv")
if not t.records:
    # TODO: الصق هنا سجلاتك — واحد واحد بالكائن الجديد
    pass
print(len(t.records))
```

4. المينيو الجديد — **نفس الثمانية خيارات** بس جسم كل خيار بقى method
   على `t`:

```python
while True:
    print("1) عرض الكل")
    print("2) إضافة سجل")
    print("3) تصفية حسب التصنيف")
    print("4) ملخص")
    print("5) بحث بالكلمة")
    print("6) حذف سجل")
    print("7) تعديل سجل")
    print("8) خروج وحفظ")
    choice = input("اختار: ")

    if choice == "1":
        for r in t.records:
            print(r)                 # يطبع النص المنسّق بدل الكائن الخام
    elif choice == "2":
        # TODO: input + try/except — ثم اعمل الكائن وأضفه
        pass
    elif choice == "3":
        category = input("التصنيف: ")
        for r in t.filter_by(category):
            print(r)
    elif choice == "4":
        print(t.summary())
    elif choice == "5":
        word = input("كلمة: ")
        for r in t.records:
            if word in str(r):
                print(r)
    elif choice == "6":
        # TODO: اعرض السجلات مرقّمة — واسأل عن الرقم واحذف من القائمة
        pass
    elif choice == "7":
        # TODO: اسأل الرقم والحقول الجديدة — وغيّر على الكائن المقصود
        pass
    elif choice == "8":
        t.save("data/sample_records.csv")
        print("اتحفظت! مع السلامة!")
        break
    else:
        print("اختيار غلط — جرّب تاني")
```

> **ملاحظة مهمة:** لو خيار 1 طبع `<tracker.models.Record object at ...>`
> يبقى `__str__` لسه ناقصة في `Record` — راجعها، لأن كل خيارات العرض
> والتصفية والبحث معتمدة عليها.

> **قبل التسليم:** **Run All** — واختار **8 (خروج وحفظ)** عشان النيوتبوك
> يقف ويحفظ ويخلص نضيف.

### تحقّق ذاتي للجزء B

**Checklist — العب كل خيار من التمانية وتأكد بنفسك:**

| الخيار | لازم يحصل |
|---|---|
| 1 | يعرض كل السجلات بشكل لطيف — مش `object at` |
| 2 | يضيف سجل حقيقي — ويرفض حقل رقمي فيه حروف برسالة واضحة |
| 3 | يعرض سجلات التصنيف المطلوب بس |
| 4 | الأرقام مطابقة للحساب اليدوي على سجلاتك |
| 5 | يلاقي سجلاً تحتويه الكلمة اللي تكتبها |
| 6 | يحذف السجل اللي تختاره فعلًا |
| 7 | يغيّر الحقل المطلوب فعلًا |
| 8 | يحفظ في الملف ويقف (break) |
| اختيار غلط | يرجع القائمة من غير ما يقع |

**تحقّق برمجي — الصقه في آخر `tracker_v3.ipynb` بعد ما تخلّص لعب:**

```python
assert isinstance(t, Tracker), "t كائن Tracker"
assert len(t.records) >= 10, "records"
assert all(isinstance(r, Record) for r in t.records), "كل سجل Record"
s = t.summary()
assert s["count"] == len(t.records), "count"
assert s["smallest"] <= s["average"] <= s["biggest"], "bounds"
t.save("data/sample_records.csv")
t2 = Tracker()
t2.load("data/sample_records.csv")
assert len(t2.records) == len(t.records), "roundtrip count"
assert isinstance(t2.records[0], Record), "roundtrip Record"
assert abs(t2.records[0].amount_egp - t.records[0].amount_egp) < 0.01, "roundtrip value"
print("Part B: ممتاز")
```

---

## الجزء C — `Tracker.top_n` (إلزامي)

ضيف طريقة `top_n` جوّا كلاس `Tracker` — ترجّع أكبر `n` سجل حسب حقل رقمي
(زي: أعلى 3 مبالغ). **اتأكد إن المسافة البادئة زي باقي الطرق** — لو
الصقتها برّا الكلاس مش هتشتغل.

```python
    # tracker/models.py — الطريقة دي تنزل جوّا كلاس المتتبّع
    def top_n(self, field, n):
        """Return the n records with the biggest value of field."""
        # TODO: لفّ على السجلات وتتبّع أكبر قيمة — ورتّبهم تنازليًا
        pass
```

**تحقق ذاتي:** الصقه في `tracker_v3.ipynb` بعد الاستيراد.

```python
sample = Tracker()
sample.add(Record("2026-10-01", "food", 85.5, "cash", 1))
sample.add(Record("2026-10-02", "drink", 40.0, "card", 2))
sample.add(Record("2026-10-03", "bills", 300.0, "card", 1))

top = sample.top_n("amount_egp", 2)
assert len(top) == 2, "top 2"
assert top[0].amount_egp == 300.0, "الأكبر أولًا"
assert top[1].amount_egp == 85.5, "الثاني"
big = sample.top_n("amount_egp", 99)
assert big[0].amount_egp == 300.0, "n أكبر من العدد"
print("Part C: ممتاز")
```

**Checklist:** جربت `n` أكبر من عدد السجلات وما وقعش · جربت حقل غير
`amount_egp` · النتيجة مرتبة تنازليًا فعلًا.

---

## التسليم — معايير القبول

| المعيار | التفاصيل |
|---|---|
| الملفات في مكانها | `tracker/models.py` في جذر الريبو · `lectures/lecture_05/exercises.ipynb` + `lectures/lecture_05/tracker_v3.ipynb` |
| الكلاسات كاملة | `Record` (الحقول الخمسة + `to_dict` + `__str__`) و `Tracker` (`add` و `filter_by` و `summary` و `save` و `load`) كلها شغالة ومعاها docstring |
| Run All نضيف | ينتهي بخروج من المينيو (خيار 8) — من غير أخطاء غير متوقعة |
| علامات ممتاز | `A1..A5` و `Part B` و `Part C` كلها طلعت |
| الخيارات التمانية | كلها شغالة فعلًا (checklist فوق) |

### إزاي ترفع `tracker/models.py` على GitHub

النيوتبوكين بيترفعوا زي كل مرة: **File → Save a copy in GitHub** في ريبو
`smart-tracker`. أما `models.py` فبيرفع من متصفح GitHub (نفس خطوات L4):

1. افتح ريبوك على github.com واضغط **Add file → Create new file**
2. اكتب المسار كامل في خانة الاسم: `tracker/models.py` (المجلدات بتعمل نفسها)
3. لصق المحتوى زي ما هو من الخلية بتاعة الـ `%%writefile` — و**Commit changes**

---

## Hand-off للمحاضرة 6

عندك دلوقتي **برنامج شغّال كامل**: كائنات ببيانات وطرق · مينيو ثمانية
خيارات · حفظ وقراءة من ملف. بس كل قرار فيه **مكتوب بإيدك** بـ `if` وقواعد
ثابتة. المحاضرة 6 — Introduction to AI: إيه لو البرنامج يقدر
**يتعلّم من البيانات ويتنبّأ** بدل ما نكتب له القواعد؟
