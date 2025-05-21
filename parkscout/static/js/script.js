// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const globalMessageArea = document.getElementById('global-message-area');

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
    
    // Enhance park card image loading
    const parkImages = document.querySelectorAll('.park-card img');
    parkImages.forEach(img => {
        img.loading = 'lazy';
        img.onerror = () => {
            const parkName = img.alt.replace('Image of ', '');
            handleImageError(img, parkName);
        };
    });

    // Add dynamic navbar shadow on scroll and animated scroll indicator
    window.addEventListener('scroll', function() {
        if (window.scrollY > 10) {
            document.body.classList.add('scrolled');
        } else {
            document.body.classList.remove('scrolled');
        }
        // Scroll progress bar
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollProgress = docHeight > 0 ? window.scrollY / docHeight : 0;
        document.body.style.setProperty('--scroll-progress', scrollProgress);
        if (!window.scrollIndicator) {
            window.scrollIndicator = document.querySelector('.scroll-indicator');
        }
        if (window.scrollIndicator) {
            if (scrollProgress > 0.01) {
                document.body.classList.add('scrolling');
            } else {
                document.body.classList.remove('scrolling');
            }
        }
    });

    // Initialize Intersection Observer for lazy loading
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                }
                observer.unobserve(img);
            }
        });
    }, {
        rootMargin: '50px 0px',
        threshold: 0.1
    });

    // Lazy load all images
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });

    // Enhanced image error handling
    async function handleImageError(img, parkName) {
        const overlay = img.closest('.image-container')?.querySelector('.image-loading-overlay');
        if (overlay) overlay.classList.remove('hidden');

        try {
            const response = await fetch(`/api/fallback-image?park=${encodeURIComponent(parkName)}`);
            if (!response.ok) throw new Error('Failed to fetch fallback image');
            
            const data = await response.json();
            if (data.url) {
                await loadImage(data.url); // Pre-load image
                img.src = data.url;
            } else {
                throw new Error('No fallback image URL');
            }
        } catch (error) {
            console.error('Image fallback error:', error);
            img.src = '/static/img/default-park.jpg';
        } finally {
            if (overlay) overlay.classList.add('hidden');
        }
    }

    // Utility function to pre-load images
    function loadImage(src) {
        return new Promise((resolve, reject) => {
            const img = new Image();
            img.onload = resolve;
            img.onerror = reject;
            img.src = src;
        });
    }

    // Smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Dark mode toggle logic
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const darkModeIcon = document.getElementById('dark-mode-icon');
    function setDarkMode(on) {
        if (on) {
            document.body.classList.add('dark');
            document.documentElement.classList.add('dark');
            localStorage.setItem('darkMode', '1');
            darkModeIcon.classList.remove('fa-moon');
            darkModeIcon.classList.add('fa-sun');
            darkModeToggle.title = "Toggle light mode";
        } else {
            document.body.classList.remove('dark');
            document.documentElement.classList.remove('dark');
            localStorage.setItem('darkMode', '0');
            darkModeIcon.classList.remove('fa-sun');
            darkModeIcon.classList.add('fa-moon');
            darkModeToggle.title = "Toggle dark mode";
        }
    }
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            setDarkMode(!document.body.classList.contains('dark'));
        });
        if (localStorage.getItem('darkMode') === '1') setDarkMode(true);
    }

    // Scroll to top button logic
    const scrollToTopBtn = document.getElementById('scroll-to-top');
    if (scrollToTopBtn) {
        scrollToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });

        // Show/hide button based on scroll position
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                scrollToTopBtn.classList.remove('hidden');
            } else {
                scrollToTopBtn.classList.add('hidden');
            }
        });
    }
}); // <-- Ensure this closing brace and parenthesis is present