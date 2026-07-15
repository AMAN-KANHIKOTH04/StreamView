import os
import re
import shutil

base_dir = r"c:\Users\amank\.gemini\antigravity-ide\scratch\StreamView"
html_dir = os.path.join(base_dir, "html")
css_dir = os.path.join(base_dir, "css")
js_dir = os.path.join(base_dir, "js")

os.makedirs(html_dir, exist_ok=True)
os.makedirs(css_dir, exist_ok=True)
os.makedirs(js_dir, exist_ok=True)

html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

tailwind_config_content = """tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      "colors": {
              "on-tertiary": "#4f2500",
              "outline": "#908fa0",
              "surface-container-lowest": "#0d0d15",
              "primary-fixed-dim": "#c0c1ff",
              "surface-bright": "#393841",
              "on-background": "#e4e1ed",
              "on-tertiary-fixed": "#301400",
              "on-secondary-container": "#d6a9ff",
              "secondary-container": "#6f00be",
              "secondary-fixed-dim": "#ddb7ff",
              "on-surface-variant": "#c7c4d7",
              "on-secondary-fixed-variant": "#6900b3",
              "secondary": "#ddb7ff",
              "primary-fixed": "#e1e0ff",
              "on-secondary-fixed": "#2c0051",
              "tertiary-fixed": "#ffdcc5",
              "inverse-primary": "#494bd6",
              "inverse-surface": "#e4e1ed",
              "on-secondary": "#490080",
              "tertiary-container": "#d97721",
              "on-surface": "#e4e1ed",
              "background": "#13131b",
              "on-primary-container": "#0d0096",
              "on-error": "#690005",
              "tertiary": "#ffb783",
              "surface-container": "#1f1f27",
              "error-container": "#93000a",
              "error": "#ffb4ab",
              "on-primary-fixed": "#07006c",
              "outline-variant": "#464554",
              "on-primary": "#1000a9",
              "surface-container-low": "#1b1b23",
              "surface-variant": "#34343d",
              "surface": "#13131b",
              "surface-container-highest": "#34343d",
              "on-primary-fixed-variant": "#2f2ebe",
              "secondary-fixed": "#f0dbff",
              "on-tertiary-fixed-variant": "#703700",
              "surface-tint": "#c0c1ff",
              "on-error-container": "#ffdad6",
              "primary": "#c0c1ff",
              "on-tertiary-container": "#452000",
              "inverse-on-surface": "#303038",
              "tertiary-fixed-dim": "#ffb783",
              "surface-dim": "#13131b",
              "primary-container": "#8083ff",
              "surface-container-high": "#292932"
      },
      "borderRadius": {
              "DEFAULT": "0.25rem",
              "lg": "0.5rem",
              "xl": "0.75rem",
              "full": "9999px"
      },
      "spacing": {
              "container-margin": "20px",
              "element-gap": "8px",
              "gutter-x": "12px",
              "section-gap": "32px"
      },
      "fontFamily": {
              "headline-lg-mobile": ["Plus Jakarta Sans"],
              "label-caps": ["Geist"],
              "body-md": ["Inter"],
              "body-sm": ["Inter"],
              "headline-xl": ["Plus Jakarta Sans"],
              "headline-lg": ["Plus Jakarta Sans"]
      },
      "fontSize": {
              "headline-lg-mobile": ["20px", { "lineHeight": "28px", "fontWeight": "700" }],
              "label-caps": ["12px", { "lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600" }],
              "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }],
              "body-sm": ["14px", { "lineHeight": "20px", "fontWeight": "400" }],
              "headline-xl": ["32px", { "lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "800" }],
              "headline-lg": ["24px", { "lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "700" }]
      }
    }
  }
}"""

styles_content = """body {
    min-height: max(884px, 100dvh);
}
.hide-scrollbar::-webkit-scrollbar,
.no-scrollbar::-webkit-scrollbar,
::-webkit-scrollbar {
    display: none;
    width: 0px;
    height: 0px;
}
.hide-scrollbar, .no-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
}
.glass-edge {
    border: 1px solid transparent;
    background: linear-gradient(180deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 100%) border-box;
    -webkit-mask: linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
}
.glass-panel {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
}
.glass-panel-heavy {
    background: rgba(19, 19, 27, 0.7);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}
.glass-overlay {
    background: linear-gradient(to top, rgba(13, 13, 21, 0.95) 0%, rgba(13, 13, 21, 0.6) 50%, rgba(13, 13, 21, 0) 100%);
}
.controls-fade, .fade-overlay {
    transition: opacity 0.4s ease-in-out;
}
.controls-hidden, .idle .fade-overlay {
    opacity: 0;
    pointer-events: none;
}
input[type=range] {
    -webkit-appearance: none;
    width: 100%;
    background: transparent;
}
input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none;
    height: 16px;
    width: 16px;
    border-radius: 50%;
    background: #c0c1ff;
    cursor: pointer;
    margin-top: -6px;
    box-shadow: 0 0 10px rgba(192, 193, 255, 0.5);
}
input[type=range]::-webkit-slider-runnable-track {
    width: 100%;
    height: 4px;
    cursor: pointer;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 2px;
}
.pb-safe { padding-bottom: env(safe-area-inset-bottom, 20px); }
.search-input:focus + .search-icon {
    color: #c0c1ff;
    text-shadow: 0 0 8px rgba(192,193,255,0.4);
}"""

main_js_content = """document.addEventListener('DOMContentLoaded', () => {
    const playerContainer = document.getElementById('player-container');
    const uiOverlay = document.getElementById('ui-overlay');
    
    if (playerContainer || uiOverlay) {
        let idleTimer;
        function resetIdleTimer() {
            if (playerContainer) playerContainer.classList.remove('idle');
            if (uiOverlay) uiOverlay.classList.remove('controls-hidden');
            clearTimeout(idleTimer);
            idleTimer = setTimeout(() => {
                if (playerContainer) playerContainer.classList.add('idle');
                if (uiOverlay) uiOverlay.classList.add('controls-hidden');
            }, 3000);
        }
        const target = playerContainer || document.body;
        target.addEventListener('mousemove', resetIdleTimer);
        target.addEventListener('touchstart', resetIdleTimer);
        target.addEventListener('click', resetIdleTimer);
        resetIdleTimer();
    }

    const progressSlider = document.getElementById('progress-slider');
    const progressFill = document.getElementById('progress-fill');
    if (progressSlider && progressFill) {
        progressSlider.addEventListener('input', (e) => {
            progressFill.style.width = e.target.value + '%';
        });
    }
});"""

with open(os.path.join(css_dir, "styles.css"), "w", encoding="utf-8") as f:
    f.write(styles_content)

with open(os.path.join(js_dir, "tailwind-config.js"), "w", encoding="utf-8") as f:
    f.write(tailwind_config_content)

with open(os.path.join(js_dir, "main.js"), "w", encoding="utf-8") as f:
    f.write(main_js_content)

for filename in html_files:
    file_path = os.path.join(base_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove script tailwind config
    content = re.sub(r'<script id="tailwind-config">[\s\S]*?</script>', '<script src="../js/tailwind-config.js"></script>', content)
    
    # Remove style tags
    content = re.sub(r'<style>[\s\S]*?</style>', '', content)
    
    # Insert styles.css link in head
    if '<head>' in content:
        content = content.replace('</head>', '    <link rel="stylesheet" href="../css/styles.css">\\n</head>')
    
    # Remove trailing script tags for logic (specifically looking for the ones containing the timer logic)
    content = re.sub(r'<script>\s*(?:const uiOverlay|// Simple idle timer)[\s\S]*?</script>', '', content)
    
    # Wait, the regex `r'<script>[\s\S]*?</script>'` above might remove tailwind CSS script itself if not careful? 
    # No, tailwind script is `<script src="...">`. It only matches tags like `<script>...`. But maybe we shouldn't do a generic match.
    # The trailing scripts in video_player have specific patterns. Let's just find <script> tags at the bottom.
    
    # Actually, tailwind script uses src. So we can remove <script> tags that don't have src.
    # We already removed <script id="tailwind-config">. So any other <script> tags without attributes can be removed.
    content = re.sub(r'<script>[\s\S]*?</script>', '', content)
    
    # Insert main.js at end of body
    if '</body>' in content:
        content = content.replace('</body>', '    <script src="../js/main.js"></script>\\n</body>')
    
    # Move to html directory
    new_path = os.path.join(html_dir, filename)
    with open(new_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Remove original file
    os.remove(file_path)

print("Refactoring complete.")
