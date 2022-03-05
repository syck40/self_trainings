import groovy.json.*
String url = 'http://api.icndb.com/jokes/random?'
def params = [limitTo:'[nerdy]', firstName:'Xavier', lastName:'Ducrohet']
String qs = params.collect { k,v -> "$k=$v" }.join('&')
String jsonTxt = "$url$qs".toURL().text
def json = new JsonSlurper().parseText(jsonTxt)
println json.value.joke
