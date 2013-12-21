function sem(n, alpha, sigma, S, callback) {
  var obj = {
    n: n,
    alpha: alpha,
    sigma: sigma,
    S: S
  };
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      callback(JSON.parse(this.responseText));
    }
  };
  xhr.open('POST', 'http://hyperinfo.viz.media.kyoto-u.ac.jp/wsgi/websem/sem');
  xhr.setRequestHeader('Content-Type', 'application/json');
  console.log(JSON.stringify(obj));
  xhr.send(JSON.stringify(obj));
}
