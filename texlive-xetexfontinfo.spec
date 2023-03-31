Name:		texlive-xetexfontinfo
Version:	15878
Release:	2
Summary:	Report font features in XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/plain/xetexfontinfo
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexfontinfo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexfontinfo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A pair of documents to reveal the font features supported by
fonts usable in XeTeX. Use OpenType-info.tex for OpenType
fonts, and AAT-info.tex for AAT fonts (Mac OS X only).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xetex/xetexfontinfo/aat-info.tex
%{_texmfdistdir}/tex/xetex/xetexfontinfo/opentype-info.tex
%doc %{_texmfdistdir}/doc/xetex/xetexfontinfo/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
