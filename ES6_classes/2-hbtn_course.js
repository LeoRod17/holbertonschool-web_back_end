export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof (name) === 'string') {
      this._name = name;
    } else {
      throw TypeError('TypeError: Name must be a string');
    }

    if (typeof (length) === 'number') {
      this._lenght = length;
    } else {
      throw TypeError('TypeError: Length must be a number');
    }

    if (Array.isArray(students)) {
      this._students = students;
    } else {
      throw TypeError('TypeError: students must be an array');
    }
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof (newName) === 'string') {
      this._name = newName;
    } else {
      throw TypeError('TypeError: Name must be a string');
    }
  }

  get length() {
    return this._lenght;
  }

  set length(newLenght) {
    if (typeof (newLenght) === 'number') {
      this._lenght = newLenght;
    } else {
      throw TypeError('TypeError: Length must be a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (Array.isArray(newStudents)) {
      this._students = newStudents;
    } else {
      throw TypeError('TypeError: students must be an array');
    }
  }
}
