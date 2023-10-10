export default function getStudentsByLocation(array, city) {
  const lista = array.filter((people) => people.location === city);
  return lista;
}
