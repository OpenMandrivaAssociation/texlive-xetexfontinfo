# revision 15878
# category Package
# catalog-ctan /macros/xetex/plain/xetexfontinfo
# catalog-date 2008-08-24 00:31:24 +0200
# catalog-license apache2
# catalog-version undef
Name:		texlive-xetexfontinfo
Version:	20080824
Release:	8
Summary:	Report font features in XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/plain/xetexfontinfo
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexfontinfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexfontinfo.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080824-2
+ Revision: 757600
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080824-1
+ Revision: 719932
- texlive-xetexfontinfo
- texlive-xetexfontinfo
- texlive-xetexfontinfo

