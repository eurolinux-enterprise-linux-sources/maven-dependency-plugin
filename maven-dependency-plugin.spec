Name:           maven-dependency-plugin
Version:        2.7
Release:        3%{?dist}
Summary:        Plugin to manipulate, copy and unpack local and remote artifacts

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         0001-Add-setThreshold-stub.patch
# Added apache-commons-io dep
Patch1:         %{name}-commons-io.patch
# Added maven-core dep
Patch2:         %{name}-core.patch
# Removed exception catching as it has already been done
# (not upstreamable)
Patch4:         %{name}-removed-exception-catching.patch

BuildArch:      noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: apache-commons-io
BuildRequires: maven-local
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-dependency-tree
BuildRequires: maven-plugin-plugin
BuildRequires: maven-plugin-annotations
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-shared-dependency-analyzer
BuildRequires: maven-shared-common-artifact-filters
BuildRequires: maven-shared-file-management
BuildRequires: maven-project
BuildRequires: maven-artifact-manager
BuildRequires: maven-plugin-testing-tools

Obsoletes: maven2-plugin-dependency <= 0:2.0.8
Provides: maven2-plugin-dependency = 1:%{version}-%{release}

%description

The dependency plugin provides the capability to manipulate
artifacts. It can copy and/or unpack artifacts from local or remote
repositories to a specified location.

%package javadoc
Group:          Documentation
Summary:        API documentation for %{name}

%description javadoc
%{summary}.


%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1

sed -i \
    's:org.codehaus.classworlds.ClassRealm:org.codehaus.plexus.classworlds.realm.ClassRealm:' \
    src/test/java/org/apache/maven/plugin/dependency/its/AbstractDependencyPluginITCase.java


%build
# Tests fail to compile because they use unsupported legacy API.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.7-3
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Mar 15 2013 Michal Srb <msrb@redhat.com> - 2.7-1
- Update to upstream version 2.7

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-1
- Update to upstream version 2.6
- Build with xmvn
- Install license files

* Tue Jan 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-2
- Remove unneeded BR: asm2

* Tue Aug 28 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-1
- Update to upstream version 2.5.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 21 2012 Tomas Radej <tradej@redhat.com> - 2.4-1
- Updated to the upstream version
- Partially removed a test because of a legacy class use
- Removed exception checking as it has already been done

* Fri Jan 13 2012 Alexander Kurtakov <akurtako@redhat.com> 2.3-3
- Add missing BR.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 11 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3-1
- Update to latest upstream

* Tue Jun 28 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2-2
- BR/R maven-shared-file-management.

* Tue Apr 26 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2-1
- Update to 2.2 final release.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.4.svn949573
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep  7 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-0.3.svn949573
- Fix test case to expect new classworlds

* Tue Jun 15 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2-0.2.svn949573
- Add missing Requires.

* Thu Jun  3 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-0.1.svn949573
- Initial package
