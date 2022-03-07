	var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
	var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
	  return new bootstrap.Popover(popoverTriggerEl)
	});



	$(document).ready(function() {

 			var myQuotes = new Array();


			myQuotes[0] = "\"The future is not something we enter. The future is something we create.\" —Leonard I. Sweet";
			myQuotes[1] = "\"If you don't think about the future, you cannot have one.\" —John Galsworthy";
			myQuotes[2] = "\"Go for it now. The future is promised to no one.\" -Wayne Dyer";
			myQuotes[3] = "\"The vast possibilities of our great future will become realities only if we make ourselves responsible for that future.\" —Gifford Pinchot";
			myQuotes[4] = "\"It was never easy to look into the future, but it is possible and we should not miss our chance.\" —Andrei Linde";
			myQuotes[5] = "\"Run to meet the future or it's going to run you down.\" —Anthony J. D'Angelo";
			myQuotes[6] = "\"The only way you can predict the future is to build it.\" -Alan Kay";
			myQuotes[7] = "\"If you don't think about the future, you cannot have one.\" -John Golsworthy";
			myQuotes[8] = "\"The present is theirs; the future, for which I really worked, is mine.\" —Nikola Tesla";
			myQuotes[9] = "\"Seek wisdom, not knowledge. Knowledge is of the past, Wisdom is of the future.\" —American Indian Proverbs";
			myQuotes[10] = "\"The empires of the future are the empires of the mind.\" —Winston Churchill";


			var myRandom = Math.floor(Math.random() * myQuotes.length);


			$("#myQuote").html(myQuotes[myRandom]);



  		});


