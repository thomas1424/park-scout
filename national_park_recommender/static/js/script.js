// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
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