import os
import django
# Setup Django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings") 
django.setup() 
 
from myapp.models import Student 
from myapp.serializers import StudentSerializer 
 
# Get one student from DB 
student = Student.objects.first() 
 
# Serialize it 
serializer = StudentSerializer(student) 
print("Serialized Data:", serializer.data) 
 
# Deserialize JSON-like data 
data = {"name": "Anitha", "marks": 21} 
serializer2 = StudentSerializer(data=data) 
 
if serializer2.is_valid(): 
    new_student = serializer2.save() 
    print("New Student Saved:", new_student) 
else: 
    print("Errors:", serializer2.errors) 