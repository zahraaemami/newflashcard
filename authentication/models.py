# 3. بررسی دسترسی حساب:
# اگر حساب کاربری‌ات ساخته شده اما دسترسی Staff ندارد:

# وارد Django shell شو:
# bash
# Copy code
# python manage.py shell
# کاربر را پیدا کن و دسترسی‌های لازم را اضافه کن:
# python
# Copy code
# from django.contrib.auth.models import User
# user = User.objects.get(username="zahra")  # نام کاربری مورد نظر
# user.is_staff = True  # فعال کردن دسترسی Staff
# user.is_superuser = True  # فعال کردن دسترسی ادمین
# user.save()
