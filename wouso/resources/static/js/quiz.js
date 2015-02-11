(function () {
	var onPageReady = function onPageReady() {
		setUpQuizPageEvents();
	};

	window.addEventListener('load', onPageReady);

	/*
	 * Quiz List Page
	 */
	var setUpQuizPageEvents = function setUpQuizPageEvents() {

		var quizList = document.getElementById('quiz-list');

		var handleClick = function handleClick(e) {
			if (e.target.hasAttribute('data-toggle')) {
				var score = e.target.parentElement.querySelector('.score');
				if (score.hasAttribute('data-visible')) {
					score.removeAttribute('data-visible');
				}
				else
					score.setAttribute('data-visible', '');
			};

		};

		quizList.addEventListener('click', handleClick);

	};
})();





