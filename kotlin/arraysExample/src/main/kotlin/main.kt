fun main()
{
    var names: Array<String> =arrayOf("Cesar","Juan","Saori")

    var numbers = arrayOf(1,2,"juanito",4,5)
    numbers[1]="b"
    //println("Element unit: ${numbers[2].length}")
    println(names[2].length)
    println("mix of elements: ${numbers[2]}")
    println("mix of elements: ${numbers[1]}")


    println("First Element: \n${names[0]}")
    names[0]="Juanito"
    println("First Element: \n${names[0]}")
    println("Number of elements: ${names.size}")

    val matrixAB= arrayOf(
        arrayOf(1,2,4),
        arrayOf(2,4,1),
        arrayOf(3,2,1))


    println("Element [1][1]: ${matrixAB[1][1]}")



}