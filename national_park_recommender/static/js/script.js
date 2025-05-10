// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-button');
    const globalMessageArea = document.getElementById('global-message-area');
    const likedCountNav = document.getElementById('liked-count-nav');
    const likedCountNavMobile = document.getElementById('liked-count-nav-mobile');

    function displayToastMessage(message, type = 'info') {
        if (!globalMessageArea) return;

        const toast = document.createElement('div');
        toast.className = `toast-message toast-${type}`;
        toast.textContent = message;
        
        globalMessageArea.appendChild(toast);

        // Trigger reflow for transition
        requestAnimationFrame(() => {
            toast.classList.add('show');
        });

        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                if (globalMessageArea.contains(toast)) {
                     globalMessageArea.removeChild(toast);
                }
            }, 300); // Wait for fade out transition
        }, 3000); // Message visible for 3 seconds
    }
    
    function updateLikedCount(newCount) {
        if (likedCountNav) {
            likedCountNav.textContent = newCount > 0 ? newCount : '';
            if (newCount > 0) {
                likedCountNav.classList.remove('hidden');
            } else {
                likedCountNav.classList.add('hidden');
            }
        }
         if (likedCountNavMobile) {
            likedCountNavMobile.textContent = newCount > 0 ? newCount : '';
            if (newCount > 0) {
                likedCountNavMobile.classList.remove('hidden');
            } else {
                likedCountNavMobile.classList.add('hidden');
            }
        }
    }


    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const parkId = this.dataset.parkId;
            const icon = this.querySelector('i.fa-heart');

            fetch(`/like_park/${parkId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // If you add CSRF protection, include the token here
                },
                // body: JSON.stringify({}) // No body needed for this simple POST
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'liked') {
                    icon.classList.remove('far', 'text-gray-600');
                    icon.classList.add('fas', 'text-red-500');
                    button.classList.add('liked');
                    button.classList.remove('unliked');
                    button.setAttribute('aria-label', `Unlike ${data.park_id}`); // A bit tricky to get park name here without another query or passing it in data attr
                } else if (data.status === 'unliked') {
                    icon.classList.remove('fas', 'text-red-500');
                    icon.classList.add('far', 'text-gray-600');
                    button.classList.remove('liked');
                    button.classList.add('unliked');
                     button.setAttribute('aria-label', `Like ${data.park_id}`);
                }
                displayToastMessage(data.message, data.status === 'liked' ? 'success' : 'info');
                
                // Update liked count in navbar (assuming session is the source of truth on next load, but can try client-side update)
                // For a more robust count update, the server could return the new total liked count.
                // For now, let's just fetch the current liked parks count or infer it.
                let currentCount = parseInt(likedCountNav.textContent || '0');
                if(data.status === 'liked') {
                    currentCount++;
                } else {
                    currentCount--;
                }
                updateLikedCount(Math.max(0, currentCount));

            })
            .catch(error => {
                console.error('Error liking park:', error);
                displayToastMessage('An error occurred. Please try again.', 'error');
            });
        });
    });

    // Mobile menu toggle (if not already in base.html or if more complex logic needed)
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', () => {
            const expanded = mobileMenuButton.getAttribute('aria-expanded') === 'true' || false;
            mobileMenuButton.setAttribute('aria-expanded', !expanded);
            mobileMenu.classList.toggle('hidden');
            const icon = mobileMenuButton.querySelector('i');
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        });
    }
}); // <-- Add this closing brace and parenthesis