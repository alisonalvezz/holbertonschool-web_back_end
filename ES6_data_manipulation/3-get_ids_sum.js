export default function getStudentsIdsSum(arrayObject) {
  return arrayObject.reduce((sum, obj) => sum + obj.id, 0)
}
