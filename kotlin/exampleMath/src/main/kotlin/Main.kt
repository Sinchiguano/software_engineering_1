fun main(args: Array<String>) {
    println("Hello World!")

    // Try adding program arguments via Run/Debug configuration.
    // Learn more about running applications: https://www.jetbrains.com/help/idea/running-applications.html.
    //println("Program arguments: ${args.joinToString()}")


    var a: Int=5
    val b: Int=3
    val result: Int=a+b
    println("The result is;"+result)
    println("The result is: $result")
    println("The result of a+b=${a+b}")
    println("The result of a/b=${a/b}")
    println("The result of a%b=${a%b}")
    println("The result of a*b=${a*b}")
    println("The result of a-b=${a-b}")

    a += 2
    println(a)
    a -=2
    println(a)
    a *=2
    println(a)
    a /=2
    println(a)
    a %=2
    println(a)
    a++
    println(a)


}