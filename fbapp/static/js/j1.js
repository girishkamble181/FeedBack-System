function validate(){
			var n= document.getElementById('id_name')
			var nr= /^[A-Za-z ]+$/
			if(! nr.test(n.value)){
				alert('name shuld contain only letters')
				n.value=""
				n.focus()
				return false

			}	
		
			return true
	}
	