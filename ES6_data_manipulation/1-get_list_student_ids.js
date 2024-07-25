export default function getListStudentsIds (arrayObject) {
  if (!Array.isArray(arrayObject)) {
    return [];
  }

  return arrayObject.map((obj) => obj.id);
}
