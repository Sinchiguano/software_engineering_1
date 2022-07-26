fun main(args: Array<String>) {
    println("Hello World!")

    // Try adding program arguments via Run/Debug configuration.
    // Learn more about running applications: https://www.jetbrains.com/help/idea/running-applications.html.
    println("Program arguments: ${args.joinToString()}")

    var a: Int=5
    var b: Int=7
    var tmp: Long=a.toLong()
    println("$tmp")

    var result: Int=a+b

    println("The sum of the numbers are: a+b= ${a+b}")



}