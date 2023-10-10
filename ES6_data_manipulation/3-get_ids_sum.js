export default function getStudentIdsSum(array) {
  const cout = array.reduce((next, currentValue) => currentValue.id + next, 0);
  return cout;
}
