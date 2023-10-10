export default function getListStudentIds(array) {
  const lista = [];
  if (Array.isArray(array)) {
    array.map((ar) => {
      lista.push(ar.id)
    });
  }
  return lista;
}
