from fastapi import FastAPI
from pydantic import BaseModel,Field


EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
PHONE_REGEX = r"^0[0-9]{9}$"

class Student_registry(BaseModel):
    full_name:str = Field(... , min_length=3)
    email:str = Field(None,pattern=EMAIL_REGEX)
    age:int = Field(... , ge= 15 , le= 60)
    phone: str = Field(None, pattern=PHONE_REGEX)
    note: str = Field(None , max_length= 200)
    


student_list = [
{
  "full_name": "Nguyen Van A",
  "email": "existing@gmail.com",
  "age": 20,
  "phone": "0987654321",
  "note" : "muon hoc lop buoi toi"
},
]

app = FastAPI()


@app.post("/students")
def add_new_student(registry:Student_registry):
    new_registry = {
            "full_name" : registry.full_name,
            "email" : registry.email,
            "age" : registry.age,
            "phone" : registry.phone,
            "note" : registry.note,

        }
    for student in student_list:
        if student['email'] == new_registry['email']:
            return{
                "detail": "Email đã tồn tại trong hệ thống"
            }


    student_list.append(new_registry)
    return{
        "message" : "thêm sinh viên thành công",
        "data" : student_list
    }
