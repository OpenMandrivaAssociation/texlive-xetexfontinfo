%global tl_name xetexfontinfo
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Report font features in XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/plain/xetexfontinfo
License:	apache2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexfontinfo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexfontinfo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A pair of documents to reveal the font features supported by fonts
usable in XeTeX. Use OpenType-info.tex for OpenType fonts, and AAT-
info.tex for AAT fonts (Mac OS X only).

