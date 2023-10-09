export default function guardrail(mathFunction) {
  const list = [];
  let ret = '';
  try {
    ret = mathFunction();
  } catch (err) {
    ret = err.toString();
  }
  list.push(ret);
  list.push('Guardrail was processed');
  return (list);
}
