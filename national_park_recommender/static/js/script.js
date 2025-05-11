// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-button');
    const globalMessageArea = document.getElementById('global-message-area');
    const likedCountNav = document.getElementById('liked-count-nav');
    const likedCountNavMobile = document.getElementById('liked-count-nav-mobile');

    function displayToastMessage(message, type = 'info') {
        const globalMessageArea = document.getElementById('global-message-area');
        if (!globalMessageArea) return;
        // Remove any existing toast messages
        globalMessageArea.querySelectorAll('.toast-message').forEach(el => el.remove());

        const toast = document.createElement('div');
        toast.className = `toast-message toast-${type}`;
        toast.textContent = message;
        globalMessageArea.appendChild(toast);
        requestAnimationFrame(() => toast.classList.add('show'));
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
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
    likeButtons.forEach(button => {
        let isProcessing = false;
        button.addEventListener('click', async function(e) {
            e.preventDefault();
            if (isProcessing) return;
            isProcessing = true;
            button.classList.add('loading');

            const parkId = button.dataset.parkId;
            const icon = button.querySelector('i');
            const label = button.querySelector('.like-btn-label');

            try {
                const response = await fetch(`/like_park/${parkId}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' }
                });
                if (!response.ok) throw new Error('Network response was not ok');
                const data = await response.json();

                // Clear any loading and state classes
                button.classList.remove('liked', 'unliked', 'loading');
                icon.classList.remove('fas', 'far');
                
                if (data.status === 'liked') {
                    button.classList.add('liked');
                    icon.classList.add('fas');
                    label.textContent = 'Added to Favorites';
                    displayToastMessage('Added to favorites!', 'success');
                } else if (data.status === 'unliked') {
                    button.classList.add('unliked');
                    icon.classList.add('far');
                    label.textContent = 'Add to Favorites';
                    displayToastMessage('Removed from favorites', 'info');
                }
                // Optionally trigger animation reset:
                icon.style.animation = 'none';
                icon.offsetHeight; // force reflow
                icon.style.animation = null;
            } catch (error) {
                console.error('Toggle favorite error:', error);
                displayToastMessage('Failed to update favorites. Please try again.', 'error');
            } finally {
                isProcessing = false;
                button.classList.remove('loading');
            }
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