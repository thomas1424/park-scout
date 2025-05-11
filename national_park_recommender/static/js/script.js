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

    // Improved like button functionality
    document.querySelectorAll('.like-button').forEach(button => {
        let isProcessing = false;

        async function toggleLike(btn) {
            if (isProcessing) return;
            
            const parkId = btn.dataset.parkId;
            const icon = btn.querySelector('i');
            const label = btn.querySelector('.like-btn-label');
            
            try {
                isProcessing = true;
                btn.classList.add('loading');
                
                const response = await fetch(`/like_park/${parkId}`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                });

                if (!response.ok) throw new Error('Network response failed');
                
                const data = await response.json();
                
                // Clear existing states
                btn.classList.remove('liked', 'unliked', 'loading');
                icon.classList.remove('fas', 'far');
                
                // Apply new state
                if (data.status === 'liked') {
                    btn.classList.add('liked');
                    icon.classList.add('fas');
                    label.textContent = 'Added to Favorites';
                    displayToastMessage('Added to favorites!', 'success');
                } else {
                    btn.classList.add('unliked');
                    icon.classList.add('far');
                    label.textContent = 'Add to Favorites';
                    displayToastMessage('Removed from favorites', 'info');
                }
                
                // Trigger heart animation
                icon.style.animation = 'none';
                icon.offsetHeight; // Trigger reflow
                icon.style.animation = null;
                
            } catch (error) {
                console.error('Error toggling like:', error);
                displayToastMessage('Failed to update favorites. Please try again.', 'error');
            } finally {
                isProcessing = false;
                btn.classList.remove('loading');
            }
        }

        button.addEventListener('click', (e) => {
            e.preventDefault();
            toggleLike(button);
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