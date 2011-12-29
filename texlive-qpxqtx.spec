# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-qpxqtx
Version:	20111104
Release:	1
Summary:	TeXLive qpxqtx package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qpxqtx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qpxqtx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive qpxqtx package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qpxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qpxbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qpxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qpxmia.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qtxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qtxbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qtxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/qpxqtx/qtxmia.tfm
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qpxbmi.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qpxbmia.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qpxmi.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qpxmia.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qtxbmi.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qtxbmia.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qtxmi.vf
%{_texmfdistdir}/fonts/vf/public/qpxqtx/qtxmia.vf
%{_texmfdistdir}/tex/generic/qpxqtx/amspbold.tex
%{_texmfdistdir}/tex/generic/qpxqtx/amsqpx.def
%{_texmfdistdir}/tex/generic/qpxqtx/amsqpx.tex
%{_texmfdistdir}/tex/generic/qpxqtx/amsqtx.def
%{_texmfdistdir}/tex/generic/qpxqtx/amsqtx.tex
%{_texmfdistdir}/tex/generic/qpxqtx/amstbold.tex
%{_texmfdistdir}/tex/generic/qpxqtx/qpxmath.sty
%{_texmfdistdir}/tex/generic/qpxqtx/qpxmath.tex
%{_texmfdistdir}/tex/generic/qpxqtx/qtxmath.sty
%{_texmfdistdir}/tex/generic/qpxqtx/qtxmath.tex
%doc %{_texmfdistdir}/doc/fonts/qpxqtx/00README
%doc %{_texmfdistdir}/doc/fonts/qpxqtx/p01tst.tex
%doc %{_texmfdistdir}/doc/fonts/qpxqtx/p02tst.tex
%doc %{_texmfdistdir}/doc/fonts/qpxqtx/qpxsymb.tex
%doc %{_texmfdistdir}/doc/fonts/qpxqtx/qpxtest.tex
%doc %{_texmfdistdir}/doc/fonts/qpxqtx/qtxsymb.tex
%doc %{_texmfdistdir}/doc/fonts/qpxqtx/qtxtest.tex
%doc %{_texmfdistdir}/doc/fonts/qpxqtx/t01tst.tex
%doc %{_texmfdistdir}/doc/fonts/qpxqtx/t02tst.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
