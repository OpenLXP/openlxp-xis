<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> dcb09cd (Testing Jack's ability to commit changes)
=======
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
>>>>>>> dcb09cd (Testing Jack's ability to commit changes)
'use strict';
{
    // Call function fn when the DOM is loaded and ready. If it is already
    // loaded, call the function now.
    // http://youmightnotneedjquery.com/#ready
    function ready(fn) {
        if (document.readyState !== 'loading') {
            fn();
        } else {
            document.addEventListener('DOMContentLoaded', fn);
        }
    }

    ready(function() {
        function handleClick(event) {
            event.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
                window.history.back(); // Go back if not a popup.
            } else {
                window.close(); // Otherwise, close the popup.
            }
        }

        document.querySelectorAll('.cancel-link').forEach(function(el) {
            el.addEventListener('click', handleClick);
        });
    });
}
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 68c08d4 (django project set up with docker and same api endpoint)
=======
>>>>>>> 86c1339 (django project set up with docker; sample api endpoint)
=======
>>>>>>> 68c08d4 (django project set up with docker and same api endpoint)
'use strict';
{
    // Call function fn when the DOM is loaded and ready. If it is already
    // loaded, call the function now.
    // http://youmightnotneedjquery.com/#ready
    function ready(fn) {
        if (document.readyState !== 'loading') {
            fn();
        } else {
            document.addEventListener('DOMContentLoaded', fn);
        }
    }

    ready(function() {
        function handleClick(event) {
            event.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
                window.history.back(); // Go back if not a popup.
            } else {
                window.close(); // Otherwise, close the popup.
            }
        }

        document.querySelectorAll('.cancel-link').forEach(function(el) {
            el.addEventListener('click', handleClick);
        });
    });
}
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 86c1339 (django project set up with docker; sample api endpoint)
=======
>>>>>>> 68c08d4 (django project set up with docker and same api endpoint)
=======
>>>>>>> dcb09cd (Testing Jack's ability to commit changes)
=======
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
>>>>>>> 86c1339 (django project set up with docker; sample api endpoint)
=======
>>>>>>> 68c08d4 (django project set up with docker and same api endpoint)
=======
>>>>>>> dcb09cd (Testing Jack's ability to commit changes)
