// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-button');
    const globalMessageArea = document.getElementById('global-message-area');
    const likedCountNav = document.getElementById('liked-count-nav');
    const likedCountNavMobile = document.getElementById('liked-count-nav-mobile');

    function displayToastMessage(message, type = 'info') {
        try {
            const globalMessageArea = document.getElementById('global-message-area');
            if (!globalMessageArea) return;

            const toast = document.createElement('div');
            toast.className = `toast-message toast-${type}`;
            toast.textContent = message;
            
            // Remove existing toasts
            const existingToasts = globalMessageArea.getElementsByClassName('toast-message');
            Array.from(existingToasts).forEach(toast => toast.remove());
            
            globalMessageArea.appendChild(toast);
            requestAnimationFrame(() => toast.classList.add('show'));

            setTimeout(() => {
                toast.classList.remove('show');
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        } catch (error) {
            console.error('Error displaying toast message:', error);
        }
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
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'liked') {
                    icon.classList.remove('far', 'text-gray-600');
                    icon.classList.add('fas', 'text-red-500');
                    button.classList.add('liked');
                    button.classList.remove('unliked');
                    button.setAttribute('aria-label', `Unlike ${data.park_id}`);
                } else if (data.status === 'unliked') {
                    icon.classList.remove('fas', 'text-red-500');
                    icon.classList.add('far', 'text-gray-600');
                    button.classList.remove('liked');
                    button.classList.add('unliked');
                    button.setAttribute('aria-label', `Like ${data.park_id}`);
                }
                displayToastMessage(data.message, data.status === 'liked' ? 'success' : 'info');
                let currentCount = parseInt(likedCountNav && likedCountNav.textContent ? likedCountNav.textContent : '0');
                if(data.status === 'liked') {
                    currentCount++;
                } else if (data.status === 'unliked' && currentCount > 0) {
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
}); // <-- Ensure this closing brace and parenthesis is present