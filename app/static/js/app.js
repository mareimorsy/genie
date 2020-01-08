
new Vue({
  el: '#app',
  data: {
    searchText: '',
    response: '',
    command: '',
    selectedPod: {'n':'', 'ns':''},
    pods: [],
    loader: false
  },
  mounted(){
  	this.fetch()
  },
  methods: {
  	fetch(){
  		this.$http.get('/api/pods').then(response => {
  		  this.pods = response.body;
  		});
  	},
  	exec(){
  		this.$http.post('/api/pod/exec', {"name": this.selectedPod.n, "namespace": this.selectedPod.ns, "command": this.command}).then(response => {
			// this.pods = response.body;
			var ansi_up = new AnsiUp;
  		  this.response = ansi_up.ansi_to_html(response.body)
  		  console.log(this.command)
  		  console.log(response.body)
  		});
  	},
  	popup(pod){
  		this.selectedPod = pod
  	},
  	filter(){
  		if (this.searchText.trim() == '') {
  			return this.pods;
  		}else{
  			self = this
  			return this.pods.filter(function(p){
  				return p.n.includes(self.searchText)
  			})
  		}
  	}
  }
})