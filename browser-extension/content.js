(function() {
	var v = new URLSearchParams(window.location.search).get('v');
	var pathName = window.location.pathname;
	var i = setInterval(function() {
		// Only if ready
		if (document.readyState !== 'complete') {
			return;
		}
		// Only interested if we watch a video or come from a video
		if (window.location.pathname != "/watch" && pathName != "/watch") {
			return;
		}
		// Reload page if video changes (hotfix, can't stop playing video)
		if (v != new URLSearchParams(window.location.search).get('v')) {
			location.reload();
		}
		// Wait until movie player is there
		if (!document.getElementById("movie_player")) {
			return;
		}
		// Check if player is still there
		if (!document.getElementById("youfucktube-player")) {
                        let iframe = document.createElement('iframe');
                        iframe.id = "youfucktube-player";
                        iframe.style = "border-left: 2px solid darkred; width: 100%; height: 100%;";
                        iframe.title="YouFuckTubePlayer";
                        iframe.frameborder="0";
                        iframe.allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
                        iframe.allowfullscreen = "1";
                        iframe.src = "https://www.youtube.com/embed/" + v;
			document.getElementById("movie_player").innerHTML = iframe.outerHTML;
		}

	}, 1000);
})()