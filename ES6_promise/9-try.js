export default function guardrail(mathFunction) {
  let list = [];
  let ret = ''
  try {
    ret = mathFunction();
  } catch (err) {
    ret = err.toString();
  }
  list.push(ret);
  list.push('Guardrail was processed')
  return (list);
}