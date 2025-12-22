# Python OOP Лабораторийн Ажил

**Зорилго:**  
Python OOP-ийг ойлгож, практик дээр код бичиж сурах  
Class, Object, Inheritance, Polymorphism, Abstraction, Encapsulation, Magic Methods-г турших

**Хугацаа:** ~1.5 цаг

---

## 1. Class & Object
**Дадлага:**
- `Student` class үүсгэж үзэх
- Attributes: `name`, `age`, `grades`
- Methods: `add_grade()`, `average_grade()`
- 3 өөр student үүсгээд дундаж оноог тооцоорой

---

## 2. Encapsulation
**Дадлага:**
- `Student` class-д private attribute нэмэх
- Getter / Setter ашиглах
- Age-г private болгоод getter/setter-ээр авах

---

## 3. Inheritance
**Дадлага:**
- `Person` class үүсгээд `Employee` child class үүсгэх
- Method override хийх
- `Student` class-г `Person`-аас удамшуулах

---

## 4. Polymorphism
**Дадлага:**
- Нэг interface, олон class ашиглах
- `Student` болон `Teacher` class-д `introduce()` method override хийх
- Polymorphism-ийг турших

---

## 5. Abstraction
**Дадлага:**
- Abstract class ашиглах (`Shape`)
- Заавал implement хийх method (`area()`)
- Rectangle болон Circle class-ийг abstract class-аас удамшуулан area-ийг тооцоолох

---

## 6. Magic Methods
**Дадлага:**
- `__str__`, `__len__`, `__eq__`, `__add__` зэрэг ашиглах
- Object-уудыг хэвлэх, харьцуулах, нийлүүлэх

---

## 7. Mini Project
**Төслийн заавар:**
- `BankAccount` system
  - Attributes: `account_number`, `owner`, `balance`
  - Methods: `deposit()`, `withdraw()`, `__str__()`
- 2–3 account үүсгэж transaction хийж үзэх
- Object-ийн мэдээллийг харьцуулж print хийх

---


**Тэмдэглэл:**  
- Өгөгдсөн сэдвүүдийг дарааллаар нь дагаж ажиллах  
- Code-ийг IDE дээр турших  
- Бүх дасгал нь объект ашиглан практик ойлголтыг бататгах зорилготой
