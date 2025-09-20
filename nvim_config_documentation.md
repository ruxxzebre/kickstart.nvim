# Neovim Configuration Documentation

## Overview
This Neovim configuration is based on **Kickstart.nvim**, a starting point for Neovim configuration that emphasizes understanding every line of code. The configuration focuses on providing essential development tools while maintaining simplicity and educational value.

## Core Configuration

### Leader Key
- **Leader key**: `<Space>` (spacebar)
- **Local leader**: `<Space>` (same as leader)

### Editor Settings
- **Tab Configuration**:
  - `tabstop = 8` (always 8, see `:h tabstop`)
  - `softtabstop = 4` (what you expect)
  - `shiftwidth = 4` (indentation width)
- **Line Numbers**: Enabled with relative numbers
- **Mouse Support**: Enabled (`mouse = 'a'`)
- **Clipboard**: Synced with OS clipboard (`clipboard = 'unnamedplus'`)
- **Search**: Case-insensitive unless uppercase letters are used
- **Undo**: Persistent undo history saved to file
- **Visual Indicators**:
  - Cursor line highlighting
  - Sign column always visible
  - Whitespace characters displayed
  - Live substitution preview

## Key Mappings

### Basic Navigation & Editing
- `jk` (Insert mode) → Exit to normal mode
- `<Esc>` (Normal mode) → Clear search highlights
- `<C-h/j/k/l>` → Navigate between windows
- `<Esc><Esc>` (Terminal mode) → Exit terminal mode

### Leader Key Combinations

#### Search Operations (`<leader>s`)
- `<leader>sh` → Search help tags
- `<leader>sk` → Search keymaps
- `<leader>sf` → Search files
- `<leader>ss` → Select Telescope picker
- `<leader>sw` → Search current word
- `<leader>sg` → Live grep search
- `<leader>sd` → Search diagnostics
- `<leader>sr` → Resume last search
- `<leader>s.` → Search recent files
- `<leader>sn` → Search Neovim config files
- `<leader>s/` → Live grep in open files
- `<leader>/` → Fuzzy search in current buffer

#### LSP Operations
- `gd` → Go to definition
- `gr` → Go to references
- `gI` → Go to implementation
- `gD` → Go to declaration
- `<leader>D` → Type definition
- `<leader>ds` → Document symbols
- `<leader>ws` → Workspace symbols
- `<leader>rn` → Rename symbol
- `<leader>ca` → Code action
- `<leader>q` → Open diagnostic quickfix list

#### Code & Formatting
- `<leader>f` → Format buffer (using Conform)

#### File Management
- `<leader><leader>` → Find existing buffers
- `\\` → Toggle NeoTree file explorer

#### Git Operations (`<leader>h`)
- `<leader>hs` → Stage hunk
- `<leader>hr` → Reset hunk
- `<leader>hS` → Stage buffer
- `<leader>hu` → Undo stage hunk
- `<leader>hR` → Reset buffer
- `<leader>hp` → Preview hunk
- `<leader>hb` → Blame line
- `<leader>hd` → Diff against index
- `<leader>hD` → Diff against last commit
- `]c` / `[c` → Jump to next/previous git change

#### Debug Operations
- `<F5>` → Start/Continue debugging
- `<F1>` → Step into
- `<F2>` → Step over
- `<F3>` → Step out
- `<F7>` → Toggle debug UI
- `<leader>b` → Toggle breakpoint
- `<leader>B` → Set conditional breakpoint

#### Toggle Operations (`<leader>t`)
- `<leader>tb` → Toggle git blame line
- `<leader>tD` → Toggle git show deleted
- `<leader>th` → Toggle inlay hints

#### Other Operations
- `<leader>a` → Toggle outline view

## Plugin Ecosystem

### Core Plugins

#### Lazy.nvim (Plugin Manager)
- **Purpose**: Plugin management and lazy loading
- **Commands**: `:Lazy` to manage plugins

#### Telescope (Fuzzy Finder)
- **Purpose**: Fuzzy finding for files, LSP symbols, grep, etc.
- **Key Features**:
  - File finding with preview
  - Live grep with regex support
  - LSP integration (definitions, references, symbols)
  - Help tag search
  - Customizable themes and layouts

#### LSP Configuration
- **LSP Server**: `lua_ls` (Lua Language Server) configured
- **TypeScript**: `typescript-tools.nvim` for enhanced TypeScript support
- **Mason**: Automatic LSP server installation
- **Features**:
  - Go to definition/references/implementation
  - Symbol search and navigation
  - Code actions and refactoring
  - Inlay hints support
  - Document highlighting

#### Treesitter
- **Purpose**: Advanced syntax highlighting and code understanding
- **Languages**: bash, c, diff, html, lua, luadoc, markdown, markdown_inline, query, vim, vimdoc
- **Features**: Auto-install new language parsers

#### Autocompletion (nvim-cmp)
- **Sources**: LSP, LuaSnip, file paths, LSP signature help
- **Snippet Engine**: LuaSnip
- **Key Bindings**:
  - `<Tab>` / `<S-Tab>` → Navigate completions
  - `<Enter>` → Accept completion
  - `<C-Space>` → Trigger completion manually
  - `<C-l>` / `<C-h>` → Navigate snippet placeholders

### Development Tools

#### Formatting (Conform)
- **Lua**: Stylua formatter
- **Auto-format**: On save (configurable per filetype)
- **Manual**: `<leader>f` to format current buffer

#### Linting (nvim-lint)
- **Markdown**: markdownlint
- **Auto-lint**: On buffer enter, write, and insert leave

#### Git Integration (Gitsigns)
- **Visual**: Git signs in gutter (`+`, `~`, `_`, etc.)
- **Hunk Operations**: Stage, reset, preview git hunks
- **Navigation**: Jump between git changes
- **Blame**: Line-by-line git blame

#### Debug Adapter Protocol (DAP)
- **Languages**: Go debugging configured with Delve
- **UI**: Beautiful debugging interface with nvim-dap-ui
- **Features**: Breakpoints, step debugging, variable inspection

### UI & Experience

#### Which-key
- **Purpose**: Shows pending keybinds as you type
- **Features**:
  - Instant keymap discovery
  - Grouped keymaps with descriptions
  - Configurable delay and icons

#### File Explorer (Neo-tree)
- **Toggle**: `\\` to open/close
- **Features**: File system browser with tree view

#### Statusline (Mini.statusline)
- **Features**: Minimal, informative status line
- **Icons**: Nerd Font icons if available
- **Location**: Shows line:column position

#### Theme
- **Colorscheme**: Tokyo Night (night variant)
- **Features**: Dark theme optimized for coding
- **Customization**: Italic comments disabled

### Additional Enhancements

#### Mini.nvim Modules
- **mini.ai**: Better around/inside textobjects
- **mini.surround**: Add/delete/replace surroundings (brackets, quotes, etc.)

#### Other Utilities
- **vim-sleuth**: Automatic tabstop and shiftwidth detection
- **todo-comments**: Highlight TODO, NOTE, etc. in comments
- **outline.nvim**: Code outline and symbol navigation
- **indent-blankline**: Indentation guides on blank lines
- **nvim-autopairs**: Automatic bracket/quote pairing
- **lazydev**: Enhanced Lua development for Neovim config

## File Structure
```
~/.config/nvim/
├── init.lua                    # Main configuration file
└── lua/kickstart/
    ├── health.lua             # Health check functions
    └── plugins/
        ├── autopairs.lua      # Auto-pairing configuration
        ├── debug.lua          # DAP debugging setup
        ├── gitsigns.lua       # Git integration keymaps
        ├── indent_line.lua    # Indentation guides
        ├── lint.lua           # Linting configuration
        └── neo-tree.lua       # File explorer setup
```

## Quick Start Commands

### Essential Commands to Learn
- `:Tutor` → Start Neovim tutorial
- `:help` → Open help system
- `:checkhealth` → Check configuration health
- `:Lazy` → Manage plugins
- `:Mason` → Manage LSP servers and tools
- `:Telescope` → Access all Telescope features

### Telescope Quick Access
- `<leader>sh` → Search help (great for learning)
- `<leader>sk` → Search keymaps (discover available shortcuts)
- `<leader>sf` → Find files quickly
- `<leader>sg` → Search in project with live grep

## Customization Tips
1. **Adding Languages**: Update LSP servers in the `servers` table in init.lua:1678
2. **Key Mappings**: Add custom keymaps after line 168 in init.lua
3. **Plugins**: Add new plugins in the lazy.setup() call around init.lua:241
4. **Formatting**: Configure formatters in conform setup around init.lua:776
5. **Linting**: Add linters in nvim-lint setup in lua/kickstart/plugins/lint.lua:8

## Learning Resources
- `:help lua-guide` → Neovim Lua guide
- `:help` → Built-in help system (use `<leader>sh` to search)
- Kickstart documentation in init.lua comments (lines 5-89)
- [Learn X in Y minutes - Lua](https://learnxinyminutes.com/docs/lua/)

This configuration provides a solid foundation for development while remaining educational and customizable. Each plugin and setting is chosen to enhance productivity without overwhelming complexity.