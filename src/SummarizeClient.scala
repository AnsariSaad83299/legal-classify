import scala.io.StdIn.readLine
import java.net.http.{HttpClient, HttpRequest, HttpResponse}
import java.net.URI
import java.net.http.HttpRequest.BodyPublishers
import java.net.http.HttpResponse.BodyHandlers

@main def runSummarizer(): Unit =
  println("Enter legal document text:")
  val input = readLine()

  val json =
    s"""{
       |  "text": "${input.replace("\"", "\\\"")}"
       |}""".stripMargin

  val request = HttpRequest.newBuilder()
    .uri(URI.create("http://localhost:5000/summarize"))  
    .header("Content-Type", "application/json")
    .POST(BodyPublishers.ofString(json))
    .build()

  val client = HttpClient.newHttpClient()
  val response = client.send(request, BodyHandlers.ofString())

  println(s"\n Summary:\n${response.body()}")
