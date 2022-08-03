fun main(args: Array<String>) {

    val names = arrayOf("Juan","Cesar","Santiago")
    val tmp = "dobryden"


    for (i in tmp){
        println(i)
    }


    for (i in names){
        println(i)
    }

    for (p in 1..10) println(p)


    for (i in 10 downTo 1) println(i)

    val namesVariable= arrayOf("ULEAM","EPN","CVUT")
    for (index in namesVariable.indices)
    {
        println("Index: $index Element: ${namesVariable[index]}")
    }

    println("##################################")
    val aVariable=false
    val bVariable=true


    println("$aVariable")
    println("${2>3}")
    println("${2==3}")
    println("${!(2==3)}")
    println("We are here: ${true||false }")

    var i =0;

while (i<=9)
    {
        println(i)
        println("$i")
        i+=1
        break

    }



for (i in 1..10)
{
    if (i>3&&i<8)
    {
        println("we found number $i")
        continue
    }
    println("$i")
}





}