export default function getStudentsByLocation(array, city) {
  let lista = array.filter((people) => people.location === city);
  return lista;
}
