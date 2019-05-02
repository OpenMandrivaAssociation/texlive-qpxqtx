Name:		texlive-qpxqtx
Version:	20190228
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
%{_texmfdistdir}/fonts/tfm/public/qpxqtx
%{_texmfdistdir}/fonts/vf/public/qpxqtx
%{_texmfdistdir}/tex/generic/qpxqtx
%doc %{_texmfdistdir}/doc/fonts/qpxqtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
