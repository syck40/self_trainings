def nums = [ 3, 2,4, 5]
nums.collect { it * 2 } //map
    .findAll { it %3 == 0 } //filter
    .sum() //reduce

```
String url = 'http://api.icndb.com/jokes/random?'
def params = [limitTo:'[nerdy]', firstName:'Xavier', lastName:'Ducrohet']
String qs = params.collect { k,v -> "$k=$v" }.join('&')
"$url$qs".toURL().text
```
