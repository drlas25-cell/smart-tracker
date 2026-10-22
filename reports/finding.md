Findings v1 — تحليل بيانات المشاكل (Project Issues)
Dataset
المصدر: data/sample_records_250.csv
الصفوف × الأعمدة: 250 صفاً × 8 أعمدة (بعد التنظيف).
الأعمدة الرئيسية: issue_id, title, priority, status, hours_spent, assigned_to, platform.
Cleaning decisions
التكرار: تم حذف صفين مكررين بالكامل لضمان دقة التحليل وعدم تكرار نفس المشاكل (انخفض عدد الصفوف من 252 إلى 250).

النواقص: تم تعويض القيم المفقودة في الأعمدة النصية بكلمة 'Unknown'

وتعبئة القيم الرقمية الناقصة بمتوسط العمود (mean) لتجنب خسارة صفوف كاملة.

أنواع غلط / outliers: تم التأكد من تناسق أنواع البيانات وخاصة العمود الرقمي الخاص بالساعات المنقضية.
Finding 1
الجملة: تعتبر منصة الويب الأكثر تسجيلاً للمشاكل بـ 53 مشكلة، تليها مباشرة تطبيقات سطح المكتب بـ 52 مشكلة.
الدليل:
         platform  issue_count
0         Web App           53
1     Desktop App           52
2      Mobile iOS           51
3  Mobile Android           48
4     Backend API           45
5         Unknown            1
Finding 2
الجملة: يتصدر المطور Sarah Ahmed قائمة مطوري الفريق من حيث متوسط الوقت المستغرق لحل المشاكل بمتوسط 20.84 ساعة تقريباً لكل مشكلة.
الدليل:
    assigned_to  average_hours_spent
9   Sarah Ahmed            20.844444
6   Omnia Ahmed            18.700202
5   Nour El-Din            18.685000
Finding 3
الجملة: المشاكل ذات الأولوية العالية (High) تستغرق في المتوسط الوقت الأطول للحل بمعدل 18.93 ساعة، متجاوزةً المشاكل الحرجة (Critical) التي يبلغ متوسط حلها 13.57 ساعة.
الدليل:
   priority  hours_spent
1      High    18.932808
3    Medium    16.877966
2       Low    15.101859
0  Critical    13.569231
Finding 4
الجملة: توزيع المشاكل متقارب جداً بين الحالات المختلفة، حيث توجد 85 مشكلة مفتوحة (Open)، و 84 مشكلة قيد العمل (In Progress)، و 81 مشكلة مغلقة بالكامل (Closed).
الدليل:
        status  issue_count
0         Open           85
1  In Progress           84
2       Closed           81
Finding 5
الجملة: المطور Fatma Omar هي الأكثر استلاماً للمشاكل في الفريق بوجود 31 مشكلة مسندة إليها، يليها Mohamed Ali بـ 26 مشكلة.
الدليل:
      assigned_to  issue_count
1      Fatma Omar           31
3     Mohamed Ali           26
7     Radwa Ahmed           25
11    Youssef Amr           25
