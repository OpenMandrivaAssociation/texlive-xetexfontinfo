# revision 15878
# category Package
# catalog-ctan /macros/xetex/plain/xetexfontinfo
# catalog-date 2008-08-24 00:31:24 +0200
# catalog-license apache2
# catalog-version undef
Name:		texlive-xetexfontinfo
Version:	20080824
Release:	1
Summary:	Report font features in XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/plain/xetexfontinfo
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexfontinfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexfontinfo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
A pair of documents to reveal the font features supported by
fonts usable in XeTeX. Use OpenType-info.tex for OpenType
fonts, and AAT-info.tex for AAT fonts (Mac OS X only).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xetex/xetexfontinfo/aat-info.tex
%{_texmfdistdir}/tex/xetex/xetexfontinfo/opentype-info.tex
%doc %{_texmfdistdir}/doc/xetex/xetexfontinfo/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
