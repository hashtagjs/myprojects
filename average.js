<!DOCTYPE html>
<html>
<body>
<script>
var n = prompt("enter a element");
sum = 0;
var arr=[];
for(var a=0;a<n;a++)
{
arr[a] = prompt("enter "+(a+1)+" st element");
sum+=parseInt(arr[a],10);
}
document.write(sum);
sum = sum/arr.length;
document.write("\n"+sum);

</script>

</body>
</html>
